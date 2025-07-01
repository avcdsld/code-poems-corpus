def register_with_http_info(vault_name, resource_group_name, fabric_name, container_name, parameters, custom_headers:nil)
      register_async(vault_name, resource_group_name, fabric_name, container_name, parameters, custom_headers:custom_headers).value!
    end