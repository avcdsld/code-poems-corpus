def get_certificate_issuers_as_lazy_with_http_info(vault_base_url, maxresults:nil, custom_headers:nil)
      get_certificate_issuers_as_lazy_async(vault_base_url, maxresults:maxresults, custom_headers:custom_headers).value!
    end