def begin_delete_by_id(resource_id, api_version, custom_headers:nil)
      response = begin_delete_by_id_async(resource_id, api_version, custom_headers:custom_headers).value!
      nil
    end