def write(key, data = nil, parameters = {}, conditions = {})
      if writable?(key, parameters, conditions)
        begin
          @memcached.set(normalize(key, parameters), data, expire_time(conditions))
          true
        rescue
          nil
        end
      end
    end