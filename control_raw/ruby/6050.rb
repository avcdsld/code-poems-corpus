def list_with_http_info(resource_group_name, private_zone_name, top:nil, recordsetnamesuffix:nil, custom_headers:nil)
      list_async(resource_group_name, private_zone_name, top:top, recordsetnamesuffix:recordsetnamesuffix, custom_headers:custom_headers).value!
    end