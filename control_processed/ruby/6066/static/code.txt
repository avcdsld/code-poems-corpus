def begin_recall_action_with_http_info(resource_group_name, storage_sync_service_name, sync_group_name, server_endpoint_name, parameters, custom_headers:nil)
      begin_recall_action_async(resource_group_name, storage_sync_service_name, sync_group_name, server_endpoint_name, parameters, custom_headers:custom_headers).value!
    end