def text_index_at_position(x, y)
      # Move caret to position the user clicks on.
      mouse_x, mouse_y = x - (self.x + padding_left), y - (self.y + padding_top)
      @char_widths.each.with_index do |width, i|
        char_x, char_y = @caret_positions[i]
        if mouse_x.between?(char_x, char_x + width) and mouse_y.between?(char_y, char_y + font.height)
          return i
        end
      end

      nil # Didn't find a character at that position.
    end