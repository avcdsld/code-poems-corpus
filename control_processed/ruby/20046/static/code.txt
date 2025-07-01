def button_params(row, col, params)
      button = Writexlsx::Package::Button.new

      button_number = 1 + @buttons_array.size

      # Set the button caption.
      caption = params[:caption] || "Button #{button_number}"

      button.font = { :_caption => caption }

      # Set the macro name.
      if params[:macro]
        button.macro = "[0]!#{params[:macro]}"
      else
        button.macro = "[0]!Button#{button_number}_Click"
      end

      # Ensure that a width and height have been set.
      default_width  = @default_col_pixels
      default_height = @default_row_pixels
      params[:width]  = default_width  if !params[:width]
      params[:height] = default_height if !params[:height]

      # Set the x/y offsets.
      params[:x_offset] = 0 if !params[:x_offset]
      params[:y_offset] = 0 if !params[:y_offset]

      # Scale the size of the comment box if required.
      if params[:x_scale]
        params[:width] = params[:width] * params[:x_scale]
      end
      if params[:y_scale]
        params[:height] = params[:height] * params[:y_scale]
      end

      # Round the dimensions to the nearest pixel.
      params[:width]  = (0.5 + params[:width]).to_i
      params[:height] = (0.5 + params[:height]).to_i

      params[:start_row] = row
      params[:start_col] = col

      # Calculate the positions of comment object.
      vertices = position_object_pixels(
                                        params[:start_col],
                                        params[:start_row],
                                        params[:x_offset],
                                        params[:y_offset],
                                        params[:width],
                                        params[:height]
                                        )

      # Add the width and height for VML.
      vertices << [params[:width], params[:height]]

      button.vertices = vertices

      button
    end