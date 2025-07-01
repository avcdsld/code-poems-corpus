def initiate_scan(resource_group_name, managed_instance_name, database_name, scan_id, custom_headers:nil)
      response = initiate_scan_async(resource_group_name, managed_instance_name, database_name, scan_id, custom_headers:custom_headers).value!
      nil
    end