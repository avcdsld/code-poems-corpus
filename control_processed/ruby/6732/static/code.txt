def wrap_key(vault_base_url, key_name, key_version, algorithm, value, custom_headers:nil)
      response = wrap_key_async(vault_base_url, key_name, key_version, algorithm, value, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end