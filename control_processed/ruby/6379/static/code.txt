def delete_application_with_http_info(application_id, force_remove:nil, timeout:60, custom_headers:nil)
      delete_application_async(application_id, force_remove:force_remove, timeout:timeout, custom_headers:custom_headers).value!
    end