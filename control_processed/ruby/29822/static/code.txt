def valid?(params, bool_response = true)
      requires params
      res = DataSift.request(:POST, 'push/validate', @config, params)
      bool_response ? res[:http][:status] == 200 : res
    end