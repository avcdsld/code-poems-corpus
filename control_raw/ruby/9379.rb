def list_by_schema(resource_group_name, server_name, database_name, schema_name, filter:nil, custom_headers:nil)
      first_page = list_by_schema_as_lazy(resource_group_name, server_name, database_name, schema_name, filter:filter, custom_headers:custom_headers)
      first_page.get_all_items
    end