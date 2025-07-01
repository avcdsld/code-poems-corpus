def observe_and_wait(*keys, &block)
      options = {:timeout => default_observe_timeout}
      options.update(keys.pop) if keys.size > 1 && keys.last.is_a?(Hash)
      verify_observe_options(options)
      raise ArgumentError, "at least one key is required" if keys.empty?
      key_cas = if keys.size == 1 && keys[0].is_a?(Hash)
                  keys[0]
                else
                  keys.flatten.each_with_object({}) do |kk, h|
                    h[kk] = nil # set CAS to nil
                  end
                end
      res = do_observe_and_wait(key_cas, options, &block) while res.nil?
      return res.values.first if keys.size == 1 && (keys[0].is_a?(String) || keys[0].is_a?(Symbol))
      return res
    end