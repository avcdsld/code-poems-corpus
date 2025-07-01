def list_by_subscription(resource_group_name, service_name, filter, top:nil, skip:nil, orderby:nil, custom_headers:nil)
      first_page = list_by_subscription_as_lazy(resource_group_name, service_name, filter, top:top, skip:skip, orderby:orderby, custom_headers:custom_headers)
      first_page.get_all_items
    end