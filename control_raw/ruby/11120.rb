def list_regional_by_resource_group_for_topic_type(resource_group_name, location, topic_type_name, filter:nil, top:nil, label:nil, custom_headers:nil)
      first_page = list_regional_by_resource_group_for_topic_type_as_lazy(resource_group_name, location, topic_type_name, filter:filter, top:top, label:label, custom_headers:custom_headers)
      first_page.get_all_items
    end