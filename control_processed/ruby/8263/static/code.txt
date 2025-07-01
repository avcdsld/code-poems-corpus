def patch(resource_group_name, cluster_name, parameters, custom_headers:nil)
      response = patch_async(resource_group_name, cluster_name, parameters, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end