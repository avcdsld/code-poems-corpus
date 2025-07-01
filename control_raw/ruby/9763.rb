def begin_create_or_update(resource_group_name, gallery_name, gallery_image_name, gallery_image, custom_headers:nil)
      response = begin_create_or_update_async(resource_group_name, gallery_name, gallery_image_name, gallery_image, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end