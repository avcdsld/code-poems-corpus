def method_missing(method, *args, &block)
      if @__receiver__.respond_to?(method.to_sym)
        @__receiver__.__send__(method.to_sym, *args, &block)
      else
        @__fallback__.__send__(method.to_sym, *args, &block)
      end
    end