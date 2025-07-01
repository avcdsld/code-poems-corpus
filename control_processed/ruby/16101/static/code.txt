def expand(behavior = nil, values = {})
      raise NotImplementedError, 'expanding not supported' unless respond_to? :expand
      @expander ||= Mustermann::Expander.new(self) { combined_ast }
      @expander.expand(behavior, values)
    end