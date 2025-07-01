def update_with_http_info(resource_group_name, vault_name, resource_resource_extended_info_details, custom_headers:nil)
      update_async(resource_group_name, vault_name, resource_resource_extended_info_details, custom_headers:custom_headers).value!
    end