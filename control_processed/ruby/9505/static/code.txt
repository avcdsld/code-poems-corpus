def trigger_with_http_info(vault_name, resource_group_name, fabric_name, container_name, protected_item_name, recovery_point_id, resource_restore_request, custom_headers:nil)
      trigger_async(vault_name, resource_group_name, fabric_name, container_name, protected_item_name, recovery_point_id, resource_restore_request, custom_headers:custom_headers).value!
    end