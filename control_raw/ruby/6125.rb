def create_or_update_with_http_info(resource_group_name, lab_account_name, lab_name, user_name, user, custom_headers:nil)
      create_or_update_async(resource_group_name, lab_account_name, lab_name, user_name, user, custom_headers:custom_headers).value!
    end