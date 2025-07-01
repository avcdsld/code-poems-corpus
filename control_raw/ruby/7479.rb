def list_by_database(location_name, long_term_retention_server_name, long_term_retention_database_name, only_latest_per_database:nil, database_state:nil, custom_headers:nil)
      first_page = list_by_database_as_lazy(location_name, long_term_retention_server_name, long_term_retention_database_name, only_latest_per_database:only_latest_per_database, database_state:database_state, custom_headers:custom_headers)
      first_page.get_all_items
    end