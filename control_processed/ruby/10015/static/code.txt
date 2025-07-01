def detect_image_with_http_info(project_id, published_name, image_data, application:nil, custom_headers:nil)
      detect_image_async(project_id, published_name, image_data, application:application, custom_headers:custom_headers).value!
    end