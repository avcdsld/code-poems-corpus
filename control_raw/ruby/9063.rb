def get_policy_properties_with_secrets(resource_group_name, account_name, content_key_policy_name, custom_headers:nil)
      response = get_policy_properties_with_secrets_async(resource_group_name, account_name, content_key_policy_name, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end