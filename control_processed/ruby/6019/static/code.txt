def begin_create_or_update(resource_group_name, certificate_order_name, certificate_distinguished_name, custom_headers:nil)
      response = begin_create_or_update_async(resource_group_name, certificate_order_name, certificate_distinguished_name, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end