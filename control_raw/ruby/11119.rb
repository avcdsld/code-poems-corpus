def list_regional_by_subscription_for_topic_type_with_http_info(location, topic_type_name, filter:nil, top:nil, label:nil, custom_headers:nil)
      list_regional_by_subscription_for_topic_type_async(location, topic_type_name, filter:filter, top:top, label:label, custom_headers:custom_headers).value!
    end