def rich_strings_fragments(rich_strings) # :nodoc:
      # Create a temp format with the default font for unformatted fragments.
      default = Format.new(0)

      length = 0                     # String length.
      last = 'format'
      pos  = 0

      fragments = []
      rich_strings.each do |token|
        if token.respond_to?(:xf_index)
          # Can't allow 2 formats in a row
          return nil if last == 'format' && pos > 0

          # Token is a format object. Add it to the fragment list.
          fragments << token
          last = 'format'
        else
          # Token is a string.
          if last != 'format'
            # If previous token wasn't a format add one before the string.
            fragments << default << token
          else
            # If previous token was a format just add the string.
            fragments << token
          end

          length += token.size    # Keep track of actual string length.
          last = 'string'
        end
        pos += 1
      end
      [fragments, length]
    end