def delete(resource_group_name, gallery_name, gallery_image_name, custom_headers:nil)
      response = delete_async(resource_group_name, gallery_name, gallery_image_name, custom_headers:custom_headers).value!
      nil
    end