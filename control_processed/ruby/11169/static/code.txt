def create_or_update(resource_group_name, gallery_name, gallery_image_name, gallery_image_version_name, gallery_image_version, custom_headers:nil)
      response = create_or_update_async(resource_group_name, gallery_name, gallery_image_name, gallery_image_version_name, gallery_image_version, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end