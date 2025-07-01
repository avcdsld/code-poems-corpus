def get_tag(project_id, tag_id, iteration_id:nil, custom_headers:nil)
      response = get_tag_async(project_id, tag_id, iteration_id:iteration_id, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end