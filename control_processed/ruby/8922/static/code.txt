def delete_custom_prebuilt_domain_with_http_info(app_id, version_id, domain_name, custom_headers:nil)
      delete_custom_prebuilt_domain_async(app_id, version_id, domain_name, custom_headers:custom_headers).value!
    end