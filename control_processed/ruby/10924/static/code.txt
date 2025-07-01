def delete_with_http_info(resource_group_name, cluster_name, extension_name, custom_headers:nil)
      delete_async(resource_group_name, cluster_name, extension_name, custom_headers:custom_headers).value!
    end