def preload(names)
      features = names.map { |name| feature(name) }
      @adapter.get_multi(features)
      features
    end