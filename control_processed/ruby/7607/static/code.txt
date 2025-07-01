def list_vips(resource_group_name, name, custom_headers:nil)
      response = list_vips_async(resource_group_name, name, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end