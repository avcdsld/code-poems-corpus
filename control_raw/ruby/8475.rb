def cancel_deletion_with_http_info(resource_group_name, account_name, certificate_name, custom_headers:nil)
      cancel_deletion_async(resource_group_name, account_name, certificate_name, custom_headers:custom_headers).value!
    end