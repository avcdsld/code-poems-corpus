def failover_commit_async(recovery_plan_name, custom_headers:nil)
      # Send request
      promise = begin_failover_commit_async(recovery_plan_name, custom_headers:custom_headers)

      promise = promise.then do |response|
        # Defining deserialization method.
        deserialize_method = lambda do |parsed_response|
          result_mapper = Azure::RecoveryServicesSiteRecovery::Mgmt::V2018_01_10::Models::RecoveryPlan.mapper()
          parsed_response = @client.deserialize(result_mapper, parsed_response)
        end

        # Waiting for response.
        @client.get_long_running_operation_result(response, deserialize_method)
      end

      promise
    end