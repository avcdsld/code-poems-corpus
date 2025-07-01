def valid?(csdl = '', boolResponse = true, service = 'facebook')
      fail BadParametersError, 'csdl is required' if csdl.empty?
      fail BadParametersError, 'service is required' if service.empty?

      params = { csdl: csdl }

      res = DataSift.request(:POST, build_path(service, 'pylon/validate', @config), @config, params)
      boolResponse ? res[:http][:status] == 200 : res
    end