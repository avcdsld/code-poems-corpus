def load(name)
      name = name.to_sym
      raise "Could not find SimpleCov Profile called '#{name}'" unless key?(name)
      SimpleCov.configure(&self[name])
    end