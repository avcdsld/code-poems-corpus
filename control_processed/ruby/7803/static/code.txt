def get_catalog(subscription_id, reserved_resource_type, location:nil, custom_headers:nil)
      response = get_catalog_async(subscription_id, reserved_resource_type, location:location, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end