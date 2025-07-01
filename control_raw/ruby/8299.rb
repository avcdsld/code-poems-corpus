def list_regional_by_subscription_for_topic_type(location, topic_type_name, custom_headers:nil)
      response = list_regional_by_subscription_for_topic_type_async(location, topic_type_name, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end