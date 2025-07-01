def list_with_http_info(resource_group_name, account_name, maxresults:nil, custom_headers:nil)
      list_async(resource_group_name, account_name, maxresults:maxresults, custom_headers:custom_headers).value!
    end