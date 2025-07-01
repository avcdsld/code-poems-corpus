def check_connectivity(resource_group_name, network_watcher_name, parameters, custom_headers:nil)
      response = check_connectivity_async(resource_group_name, network_watcher_name, parameters, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end