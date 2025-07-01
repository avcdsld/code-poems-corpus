def create_or_update_with_http_info(resource_group_name, resource_provider_namespace, parent_resource_path, resource_type, resource_name, api_version, parameters, custom_headers:nil)
      create_or_update_async(resource_group_name, resource_provider_namespace, parent_resource_path, resource_type, resource_name, api_version, parameters, custom_headers:custom_headers).value!
    end