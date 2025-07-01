def delete(identity_id = '', service = '')
      fail BadParametersError, 'identity_id is required' if identity_id.empty?
      fail BadParametersError, 'service is required' if service.empty?

      DataSift.request(:DELETE, "account/identity/#{identity_id}/limit/#{service}", @config)
    end