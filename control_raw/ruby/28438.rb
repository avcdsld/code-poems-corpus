def **(n)
      if @expr.nil?
        expr = nil
      elsif /^[A-Za-z_]+$/o =~ @expr
        expr = @expr+'^'+n.to_s
      else
        expr = '('+@expr+')^'+n.to_s+''
      end
      self.class.new( @value**n, expr, @unit**n )
    end