def list_by_resource_group(resource_group_name, api_version, subscription_id, custom_headers:nil)
      response = list_by_resource_group_async(resource_group_name, api_version, subscription_id, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end