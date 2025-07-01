def list_deployments_at_subscription(remediation_name, query_options:nil, custom_headers:nil)
      first_page = list_deployments_at_subscription_as_lazy(remediation_name, query_options:query_options, custom_headers:custom_headers)
      first_page.get_all_items
    end