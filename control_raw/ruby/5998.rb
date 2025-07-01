def update_with_http_info(resource_group_name, certificate_order_name, certificate_distinguished_name, custom_headers:nil)
      update_async(resource_group_name, certificate_order_name, certificate_distinguished_name, custom_headers:custom_headers).value!
    end