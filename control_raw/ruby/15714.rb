def []=(key, value)
      raise_if_ignored

      unless WRITABLE_KEYS.include?(key)
        raise Airbrake::Error,
              ":#{key} is not recognized among #{WRITABLE_KEYS}"
      end

      unless value.respond_to?(:to_hash)
        raise Airbrake::Error, "Got #{value.class} value, wanted a Hash"
      end

      @payload[key] = value.to_hash
    end