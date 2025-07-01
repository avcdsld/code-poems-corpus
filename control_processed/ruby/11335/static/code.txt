def match_file_input_with_http_info(image_stream, list_id:nil, cache_image:nil, custom_headers:nil)
      match_file_input_async(image_stream, list_id:list_id, cache_image:cache_image, custom_headers:custom_headers).value!
    end