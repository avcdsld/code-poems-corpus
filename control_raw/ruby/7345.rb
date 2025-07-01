def add_storage_account(resource_group_name, account_name, storage_account_name, parameters, custom_headers:nil)
      response = add_storage_account_async(resource_group_name, account_name, storage_account_name, parameters, custom_headers:custom_headers).value!
      nil
    end