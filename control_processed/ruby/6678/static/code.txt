def list_by_instance_pool(resource_group_name, instance_pool_name, custom_headers:nil)
      first_page = list_by_instance_pool_as_lazy(resource_group_name, instance_pool_name, custom_headers:custom_headers)
      first_page.get_all_items
    end