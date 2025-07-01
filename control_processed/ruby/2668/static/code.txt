def list(path, params = {}, headers = {})
      params = params.merge(list: true)
      request(:get, path, params, headers)
    end