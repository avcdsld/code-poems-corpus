def create_async(subscription_definition_name, body, custom_headers:nil)
      # Send request
      promise = begin_create_async(subscription_definition_name, body, custom_headers:custom_headers)

      promise = promise.then do |response|
        # Defining deserialization method.
        deserialize_method = lambda do |parsed_response|
          result_mapper = Azure::Subscriptions::Mgmt::V2017_11_01_preview::Models::SubscriptionDefinition.mapper()
          parsed_response = @client.deserialize(result_mapper, parsed_response)
        end

        # Waiting for response.
        @client.get_long_running_operation_result(response, deserialize_method)
      end

      promise
    end