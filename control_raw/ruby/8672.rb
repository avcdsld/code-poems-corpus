def create_or_update_with_http_info(resource_group_name, vault_name, vault, custom_headers:nil)
      create_or_update_async(resource_group_name, vault_name, vault, custom_headers:custom_headers).value!
    end