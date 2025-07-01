def varargs_type
      if @input.scan(/\.\.\./)
        varargs = true
        @out << "..."
        if @input.scan(/\[/)
          varargs_bracketed = true
          @out << "["
        end
      end

      return false unless null_type

      if !varargs
        @out << "..." if @input.scan(/\.\.\./)
      end

      if varargs_bracketed
        return false unless @input.scan(/\]/)
        @out << "]"
      end

      true
    end