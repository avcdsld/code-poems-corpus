def update_publish_settings(app_id, publish_setting_update_object, custom_headers:nil)
      response = update_publish_settings_async(app_id, publish_setting_update_object, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end