def delete_management_policies(resource_group_name, account_name, custom_headers:nil)
      response = delete_management_policies_async(resource_group_name, account_name, custom_headers:custom_headers).value!
      nil
    end