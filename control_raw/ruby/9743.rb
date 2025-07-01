def begin_stop(resource_group_name, lab_account_name, lab_name, environment_setting_name, environment_name, custom_headers:nil)
      response = begin_stop_async(resource_group_name, lab_account_name, lab_name, environment_setting_name, environment_name, custom_headers:custom_headers).value!
      nil
    end