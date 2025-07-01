def resume_async(resource_group_name, server_name, database_name, custom_headers:nil)
      # Send request
      promise = begin_resume_async(resource_group_name, server_name, database_name, custom_headers:custom_headers)

      promise = promise.then do |response|
        # Defining deserialization method.
        deserialize_method = lambda do |parsed_response|
        end

        # Waiting for response.
        @client.get_long_running_operation_result(response, deserialize_method)
      end

      promise
    end