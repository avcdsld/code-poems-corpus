def list_global_by_resource_group_for_topic_type(resource_group_name, topic_type_name, custom_headers:nil)
      response = list_global_by_resource_group_for_topic_type_async(resource_group_name, topic_type_name, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end