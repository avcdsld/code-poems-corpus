def site_data_from_results(res, sitename, key)
      sites = res['sites']
      sites.each do |site|
        return site[key] if site['site'] == sitename
      end
      nil
    end