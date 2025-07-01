def classify_image_url_with_no_store_with_http_info(project_id, published_name, image_url, application:nil, custom_headers:nil)
      classify_image_url_with_no_store_async(project_id, published_name, image_url, application:application, custom_headers:custom_headers).value!
    end