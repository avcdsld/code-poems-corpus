def delete_with_http_info(resource_group_name, service_name, opid, if_match, custom_headers:nil)
      delete_async(resource_group_name, service_name, opid, if_match, custom_headers:custom_headers).value!
    end