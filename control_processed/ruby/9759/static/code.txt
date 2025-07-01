def create_or_update_async(resource_group_name, gallery_name, gallery_image_name, gallery_image, custom_headers:nil)
      # Send request
      promise = begin_create_or_update_async(resource_group_name, gallery_name, gallery_image_name, gallery_image, custom_headers:custom_headers)

      promise = promise.then do |response|
        # Defining deserialization method.
        deserialize_method = lambda do |parsed_response|
          result_mapper = Azure::Compute::Mgmt::V2018_06_01::Models::GalleryImage.mapper()
          parsed_response = @client.deserialize(result_mapper, parsed_response)
        end

        # Waiting for response.
        @client.get_long_running_operation_result(response, deserialize_method)
      end

      promise
    end