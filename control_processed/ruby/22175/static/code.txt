def draw_foreground
      # Always roll back changes made by the user unless the text is editable.
      if editable? or text == @old_text
        recalc if focused? # Workaround for Windows draw/update bug.
        @old_caret_position = caret_position
        @old_selection_start = @text_input.selection_start
      else
        roll_back
      end

      if caret_position > stripped_text.length
        self.caret_position = stripped_text.length
      end

      if @text_input.selection_start >= stripped_text.length
        @text_input.selection_start = stripped_text.length
      end

      # Draw the selection.
      selection_range.each do |pos|
        char_x, char_y = @caret_positions[pos]
        char_width = @char_widths[pos]
        left, top = x + padding_left + char_x, y + padding_top + char_y
        draw_rect left, top, char_width, font.height, z, @selection_color
      end

      # Draw text.
      @lines.each_with_index do |line, index|
        font.draw(line, x + padding_left, y + padding_top + y_at_line(index), z)
      end

      # Draw the caret.
      if focused? and ((Gosu::milliseconds / @caret_period) % 2 == 0)
        caret_x, caret_y = @caret_positions[caret_position]
        left, top = x + padding_left + caret_x, y + padding_top + caret_y
        draw_rect left, top, 1, font.height, z, @caret_color
      end
    end