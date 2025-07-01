def create_and_start_migration_async(resource_group_name, namespace_name, parameters, custom_headers:nil)
      # Send request
      promise = begin_create_and_start_migration_async(resource_group_name, namespace_name, parameters, custom_headers:custom_headers)

      promise = promise.then do |response|
        # Defining deserialization method.
        deserialize_method = lambda do |parsed_response|
          result_mapper = Azure::ServiceBus::Mgmt::V2017_04_01::Models::MigrationConfigProperties.mapper()
          parsed_response = @client.deserialize(result_mapper, parsed_response)
        end

        # Waiting for response.
        @client.get_long_running_operation_result(response, deserialize_method)
      end

      promise
    end