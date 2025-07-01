def begin_create_or_update_certificate_with_http_info(resource_group_name, certificate_order_name, name, key_vault_certificate, custom_headers:nil)
      begin_create_or_update_certificate_async(resource_group_name, certificate_order_name, name, key_vault_certificate, custom_headers:custom_headers).value!
    end