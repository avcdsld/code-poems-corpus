def list_by_subscription(skiptoken:nil, custom_headers:nil)
      first_page = list_by_subscription_as_lazy(skiptoken:skiptoken, custom_headers:custom_headers)
      first_page.get_all_items
    end