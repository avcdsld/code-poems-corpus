def fetch(*args)
      raise ArgumentError, "Expected 1-2 arguments, got #{args.length}" \
        unless (1..2).cover?(args.length)

      key, default = args

      all(key) do |value|
        return value
      end

      if block_given?
        yield key
      elsif default
        default
      else
        raise KeyError, "key not found: #{key.inspect}"
      end
    end