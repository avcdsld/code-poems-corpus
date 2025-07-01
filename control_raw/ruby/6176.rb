def begin_reimage(resource_group_name, vm_scale_set_name, custom_headers:nil)
      response = begin_reimage_async(resource_group_name, vm_scale_set_name, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end