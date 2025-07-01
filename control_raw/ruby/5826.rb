def get(user)
      mechanism = user.mechanism
      raise InvalidMechanism.new(mechanism) if !SOURCES.has_key?(mechanism)
      SOURCES[mechanism].new(user)
    end