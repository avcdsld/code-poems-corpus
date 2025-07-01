def create(name, sites, groups, internal_domain_prefix = nil)
      sites = Array(sites)
      groups = Array(groups)
      current_path = '/api/v1/collections'
      payload = { 'name' => name, 'site_ids' => sites, 'group_ids' => groups,
                  'internal_domain_prefix' => internal_domain_prefix }.to_json
      @conn.post(current_path, payload)
    end