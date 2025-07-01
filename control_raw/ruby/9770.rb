def change_controller_power_state_async(device_name, hardware_component_group_name, parameters, resource_group_name, manager_name, custom_headers:nil)
      # Send request
      promise = begin_change_controller_power_state_async(device_name, hardware_component_group_name, parameters, resource_group_name, manager_name, custom_headers:custom_headers)

      promise = promise.then do |response|
        # Defining deserialization method.
        deserialize_method = lambda do |parsed_response|
        end

        # Waiting for response.
        @client.get_long_running_operation_result(response, deserialize_method)
      end

      promise
    end