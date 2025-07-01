def list_persisted_scripts(resource_group_name, cluster_name, custom_headers:nil)
      first_page = list_persisted_scripts_as_lazy(resource_group_name, cluster_name, custom_headers:custom_headers)
      first_page.get_all_items
    end