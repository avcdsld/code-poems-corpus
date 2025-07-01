def all
      response = request(:get_all)
      handles = response.values.flatten.collect { |handle| Entity::Handle.build(handle) }
      get_data_for_handles(handles)

      self
    end