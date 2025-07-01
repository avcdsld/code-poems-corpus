def add_filter(detach_with_id, filter_code)
      raise WiceGridException.new("Detached ID #{detach_with_id} is already used!") if @filters.key? detach_with_id
      @filters[detach_with_id] = filter_code
    end