def update_application_upgrade(application_id, application_upgrade_update_description, timeout:60, custom_headers:nil)
      response = update_application_upgrade_async(application_id, application_upgrade_update_description, timeout:timeout, custom_headers:custom_headers).value!
      nil
    end