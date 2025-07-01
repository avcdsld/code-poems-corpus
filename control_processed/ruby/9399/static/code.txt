def list_container_sas_with_http_info(resource_group_name, account_name, asset_name, parameters, custom_headers:nil)
      list_container_sas_async(resource_group_name, account_name, asset_name, parameters, custom_headers:custom_headers).value!
    end