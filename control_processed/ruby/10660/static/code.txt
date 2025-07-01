def update(resource_group_name, account_name, sku:nil, tags:nil, properties:nil, custom_headers:nil)
      response = update_async(resource_group_name, account_name, sku:sku, tags:tags, properties:properties, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end