def reorder_rtl_content(text)
      rtl_characters = "\u05d0-\u05ea\u05f0-\u05f4\u0600-\u06ff\u0750-\u077f"
      rtl_replaces = { '(' => ')', ')' => '(',
                       '[' => ']', ']' => '[',
                       '{' => '}', '}' => '{',
                       '<' => '>', '>' => '<' }
      return text unless text =~ /[#{rtl_characters}]/

      out = []
      scanner = StringScanner.new text
      until scanner.eos?
        if scanner.scan(/[#{rtl_characters} ]/)
          out.unshift scanner.matched
        elsif scanner.scan(/[^#{rtl_characters}]+/)
          if out.empty? && scanner.matched.match(/[\s]$/) && !scanner.eos?
            white_space_to_move = scanner.matched.match(/[\s]+$/).to_s
            out.unshift scanner.matched[0..-1 - white_space_to_move.length]
            out.unshift white_space_to_move
          elsif scanner.matched =~ /^[\(\)\[\]\{\}\<\>]$/
            out.unshift rtl_replaces[scanner.matched]
          else
            out.unshift scanner.matched
          end
        end
      end
      out.join.strip
    end