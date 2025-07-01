def resume(resource_group_name, name, custom_headers:nil)
      first_page = resume_as_lazy(resource_group_name, name, custom_headers:custom_headers)
      first_page.get_all_items
    end