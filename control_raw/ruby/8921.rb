def delete_custom_prebuilt_domain(app_id, version_id, domain_name, custom_headers:nil)
      response = delete_custom_prebuilt_domain_async(app_id, version_id, domain_name, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end