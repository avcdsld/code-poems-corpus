def _fetch_remote_rest_apis(provider)
      cache = GeoEngineer::ApiGatewayHelpers._rest_api_cache
      return cache[provider] if cache[provider]

      ret = _client(provider).get_rest_apis['items'].map(&:to_h).map do |rr|
        rr[:_terraform_id]    = rr[:id]
        rr[:_geo_id]          = rr[:name]
        rr[:root_resource_id] = _root_resource_id(provider, rr)
        rr
      end.compact
      cache[provider] = ret
      ret
    end