def method_missing(method_symbol, *args)
      method_symbol = $1.to_sym if method_symbol.to_s =~ /(.+)=$/
      internal_get_or_set(method_symbol, *args)
    end