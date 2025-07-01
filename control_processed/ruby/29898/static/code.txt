def get_providers(security_filter = nil,
                      name_filter = nil,
                      show_only_providers_flag = "Y",
                      internal_external = "I",
                      ordering_authority = nil,
                      real_provider = "N")
      params =
        MagicParams.format(
          parameter1: security_filter,
          parameter2: name_filter,
          parameter3: show_only_providers_flag,
          parameter4: internal_external,
          parameter5: ordering_authority,
          parameter6: real_provider
        )
      results = magic("GetProviders", magic_params: params)
      results["getprovidersinfo"]
    end