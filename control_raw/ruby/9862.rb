def create_or_update(resource_group_name, gallery_name, gallery, custom_headers:nil)
      response = create_or_update_async(resource_group_name, gallery_name, gallery, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end