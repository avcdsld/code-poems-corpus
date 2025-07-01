def get_with_http_info(resource_group_name, vm_name, vm_extension_name, expand:nil, custom_headers:nil)
      get_async(resource_group_name, vm_name, vm_extension_name, expand:expand, custom_headers:custom_headers).value!
    end