def update_with_http_info(app_id, version_id, list_of_app_version_setting_object, custom_headers:nil)
      update_async(app_id, version_id, list_of_app_version_setting_object, custom_headers:custom_headers).value!
    end