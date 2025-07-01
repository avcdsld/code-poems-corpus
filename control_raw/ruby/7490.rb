def create_key(vault_base_url, key_name, kty, key_size:nil, key_ops:nil, key_attributes:nil, tags:nil, custom_headers:nil)
      response = create_key_async(vault_base_url, key_name, kty, key_size:key_size, key_ops:key_ops, key_attributes:key_attributes, tags:tags, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end