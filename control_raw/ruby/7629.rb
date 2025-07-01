def list_multi_role_pool_skus(resource_group_name, name, custom_headers:nil)
      first_page = list_multi_role_pool_skus_as_lazy(resource_group_name, name, custom_headers:custom_headers)
      first_page.get_all_items
    end