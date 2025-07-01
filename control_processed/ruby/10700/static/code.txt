def begin_update_by_id(resource_id, api_version, parameters, custom_headers:nil)
      response = begin_update_by_id_async(resource_id, api_version, parameters, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end