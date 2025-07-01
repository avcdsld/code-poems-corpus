def get(vault_name, resource_group_name, filter:nil, skip_token:nil, custom_headers:nil)
      first_page = get_as_lazy(vault_name, resource_group_name, filter:filter, skip_token:skip_token, custom_headers:custom_headers)
      first_page.get_all_items
    end