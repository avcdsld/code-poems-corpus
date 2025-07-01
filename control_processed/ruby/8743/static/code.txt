def get_tagged_image_count(project_id, iteration_id:nil, tag_ids:nil, custom_headers:nil)
      response = get_tagged_image_count_async(project_id, iteration_id:iteration_id, tag_ids:tag_ids, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end