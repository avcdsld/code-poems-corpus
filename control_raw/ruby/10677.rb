def run_async(resource_group_name, workflow_name, parameters, custom_headers:nil)
      # Send request
      promise = begin_run_async(resource_group_name, workflow_name, parameters, custom_headers:custom_headers)

      promise = promise.then do |response|
        # Defining deserialization method.
        deserialize_method = lambda do |parsed_response|
          result_mapper = Azure::Logic::Mgmt::V2015_02_01_preview::Models::WorkflowRun.mapper()
          parsed_response = @client.deserialize(result_mapper, parsed_response)
        end

        # Waiting for response.
        @client.get_long_running_operation_result(response, deserialize_method)
      end

      promise
    end