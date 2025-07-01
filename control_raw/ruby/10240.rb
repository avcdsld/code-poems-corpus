def create_or_update(resource_uri, association_name, diagnostic_settings_association, custom_headers:nil)
      response = create_or_update_async(resource_uri, association_name, diagnostic_settings_association, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end