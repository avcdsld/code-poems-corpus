def start_async(resource_group_name, job_name, start_job_parameters:nil, custom_headers:nil)
      # Send request
      promise = begin_start_async(resource_group_name, job_name, start_job_parameters:start_job_parameters, custom_headers:custom_headers)

      promise = promise.then do |response|
        # Defining deserialization method.
        deserialize_method = lambda do |parsed_response|
        end

        # Waiting for response.
        @client.get_long_running_operation_result(response, deserialize_method)
      end

      promise
    end