def list_by_hub_with_http_info(resource_group_name, hub_name, locale_code:'en-us', custom_headers:nil)
      list_by_hub_async(resource_group_name, hub_name, locale_code:locale_code, custom_headers:custom_headers).value!
    end