def begin_create_or_update_certificate(resource_group_name, certificate_order_name, name, key_vault_certificate, custom_headers:nil)
      response = begin_create_or_update_certificate_async(resource_group_name, certificate_order_name, name, key_vault_certificate, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end