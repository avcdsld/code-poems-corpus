def shorten(original_chars, chars, length_without_trailing)
      truncated = []
      char_width = display_width(chars[0])
      while length_without_trailing - char_width > 0
        orig_char = original_chars.shift
        char = chars.shift
        break unless char
        while orig_char != char # consume ansi
          ansi = true
          truncated << orig_char
          orig_char = original_chars.shift
        end
        truncated << char
        char_width = display_width(char)
        length_without_trailing -= char_width
      end
      truncated << ["\e[0m"] if ansi
      truncated
    end