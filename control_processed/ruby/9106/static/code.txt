def pre_backup_async(resource_group_name, storage_sync_service_name, sync_group_name, cloud_endpoint_name, parameters, custom_headers:nil)
      # Send request
      promise = begin_pre_backup_async(resource_group_name, storage_sync_service_name, sync_group_name, cloud_endpoint_name, parameters, custom_headers:custom_headers)

      promise = promise.then do |response|
        # Defining deserialization method.
        deserialize_method = lambda do |parsed_response|
        end

        # Waiting for response.
        @client.get_long_running_operation_result(response, deserialize_method)
      end

      promise
    end