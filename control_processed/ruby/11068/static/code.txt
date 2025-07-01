def set_flow_log_configuration_async(resource_group_name, network_watcher_name, parameters, custom_headers:nil)
      # Send request
      promise = begin_set_flow_log_configuration_async(resource_group_name, network_watcher_name, parameters, custom_headers:custom_headers)

      promise = promise.then do |response|
        # Defining deserialization method.
        deserialize_method = lambda do |parsed_response|
          result_mapper = Azure::Network::Mgmt::V2018_10_01::Models::FlowLogInformation.mapper()
          parsed_response = @client.deserialize(result_mapper, parsed_response)
        end

        # Waiting for response.
        @client.get_long_running_operation_result(response, deserialize_method)
      end

      promise
    end