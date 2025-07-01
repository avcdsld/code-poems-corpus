def create_with_http_info(resource_group_name, account_name, container_name, blob_container, custom_headers:nil)
      create_async(resource_group_name, account_name, container_name, blob_container, custom_headers:custom_headers).value!
    end