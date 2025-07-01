def get_data_lake_store_account(resource_group_name, account_name, data_lake_store_account_name, custom_headers:nil)
      response = get_data_lake_store_account_async(resource_group_name, account_name, data_lake_store_account_name, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end