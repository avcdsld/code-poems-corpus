def method_missing(symbol)
      if hash.key?(symbol)
        hash[symbol]
      elsif hash.key?(symbol.to_s)
        hash[symbol.to_s]
      else
        raise NoMethodError
      end
    end