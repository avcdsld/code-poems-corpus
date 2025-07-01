def new(relation, new_options = EMPTY_HASH)
      self.class.new(relation, new_options.empty? ? options : options.merge(new_options))
    end