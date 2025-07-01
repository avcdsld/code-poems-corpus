def list_locations(subscription_id, custom_headers:nil)
      response = list_locations_async(subscription_id, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end