def backup_key(vault_base_url, key_name, custom_headers:nil)
      response = backup_key_async(vault_base_url, key_name, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end