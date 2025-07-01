def create_or_update_at_subscription_scope_async(deployment_name, parameters, custom_headers:nil)
      # Send request
      promise = begin_create_or_update_at_subscription_scope_async(deployment_name, parameters, custom_headers:custom_headers)

      promise = promise.then do |response|
        # Defining deserialization method.
        deserialize_method = lambda do |parsed_response|
          result_mapper = Azure::Resources::Mgmt::V2018_05_01::Models::DeploymentExtended.mapper()
          parsed_response = @client.deserialize(result_mapper, parsed_response)
        end

        # Waiting for response.
        @client.get_long_running_operation_result(response, deserialize_method)
      end

      promise
    end