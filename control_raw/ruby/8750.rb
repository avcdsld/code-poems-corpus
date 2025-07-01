def delete_image_regions(project_id, region_ids, custom_headers:nil)
      response = delete_image_regions_async(project_id, region_ids, custom_headers:custom_headers).value!
      nil
    end