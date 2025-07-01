def purge_deleted_async(vault_name, location, custom_headers:nil)
      # Send request
      promise = begin_purge_deleted_async(vault_name, location, custom_headers:custom_headers)

      promise = promise.then do |response|
        # Defining deserialization method.
        deserialize_method = lambda do |parsed_response|
        end

        # Waiting for response.
        @client.get_long_running_operation_result(response, deserialize_method)
      end

      promise
    end