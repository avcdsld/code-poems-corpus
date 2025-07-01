def stop(resource_group_name, network_watcher_name, connection_monitor_name, custom_headers:nil)
      response = stop_async(resource_group_name, network_watcher_name, connection_monitor_name, custom_headers:custom_headers).value!
      nil
    end