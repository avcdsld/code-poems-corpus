def compile
      parse

      @fragments = re_raise_with_location { process(@sexp).flatten }
      @fragments << fragment("\n", nil, s(:newline)) unless @fragments.last.code.end_with?("\n")

      @result = @fragments.map(&:code).join('')
    end