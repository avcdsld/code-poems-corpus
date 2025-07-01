def begin_download_with_http_info(resource_group_name, virtual_wanname, request, custom_headers:nil)
      begin_download_async(resource_group_name, virtual_wanname, request, custom_headers:custom_headers).value!
    end