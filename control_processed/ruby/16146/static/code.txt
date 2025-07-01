def models(klass)
      return @models if defined? @models
      return [] if frozen?

      # Use select_all to retrieve hashes for each row instead of arrays of values.
      @models = connection.
        select_all(query, "#{klass.name} Load via #{self.class.name}").
          collect! { |record| klass.send :instantiate, record }

      retrieve_found_row_count
      freeze

      @models
    end