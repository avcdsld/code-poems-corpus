def list_callback_url_with_http_info(resource_group_name, integration_account_name, parameters, custom_headers:nil)
      list_callback_url_async(resource_group_name, integration_account_name, parameters, custom_headers:custom_headers).value!
    end