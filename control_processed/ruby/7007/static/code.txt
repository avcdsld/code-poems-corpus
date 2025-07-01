def get(location, api_version, subscription_id, cluster_version, custom_headers:nil)
      response = get_async(location, api_version, subscription_id, cluster_version, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end