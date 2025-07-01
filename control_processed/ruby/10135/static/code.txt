def get_deleted_sas_definitions_as_lazy_with_http_info(vault_base_url, storage_account_name, maxresults:nil, custom_headers:nil)
      get_deleted_sas_definitions_as_lazy_async(vault_base_url, storage_account_name, maxresults:maxresults, custom_headers:custom_headers).value!
    end