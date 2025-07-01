def update(id, hash = '', name = '', service = 'facebook')
      fail BadParametersError, 'service is required' if service.empty?

      params = { id: id }
      params.merge!(hash: hash) unless hash.empty?
      params.merge!(name: name) unless name.empty?

      DataSift.request(:PUT, build_path(service, 'pylon/update', @config), @config, params)
    end