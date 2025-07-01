def replace_key_exp(key, replacement)
      scanner = StringScanner.new(key)
      braces  = []
      result  = []
      while (match_until = scanner.scan_until(/(?:#?\{|})/))
        if scanner.matched == '#{'
          braces << scanner.matched
          result << match_until[0..-3] if braces.length == 1
        elsif scanner.matched == '}'
          prev_brace = braces.pop
          result << replacement if braces.empty? && prev_brace == '#{'
        else
          braces << '{'
        end
      end
      result << key[scanner.pos..-1] unless scanner.eos?
      result.join
    end