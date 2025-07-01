def begin_update_with_http_info(resource_group_name, topic_name, topic_update_parameters, custom_headers:nil)
      begin_update_async(resource_group_name, topic_name, topic_update_parameters, custom_headers:custom_headers).value!
    end