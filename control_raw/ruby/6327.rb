def provision_cluster_async(provision_fabric_description, timeout:60, custom_headers:nil)
      api_version = '6.0'
      fail ArgumentError, 'provision_fabric_description is nil' if provision_fabric_description.nil?
      fail ArgumentError, "'timeout' should satisfy the constraint - 'InclusiveMaximum': '4294967295'" if !timeout.nil? && timeout > 4294967295
      fail ArgumentError, "'timeout' should satisfy the constraint - 'InclusiveMinimum': '1'" if !timeout.nil? && timeout < 1


      request_headers = {}
      request_headers['Content-Type'] = 'application/json; charset=utf-8'

      # Set Headers
      request_headers['x-ms-client-request-id'] = SecureRandom.uuid
      request_headers['accept-language'] = accept_language unless accept_language.nil?

      # Serialize Request
      request_mapper = Azure::ServiceFabric::V6_2_0_9::Models::ProvisionFabricDescription.mapper()
      request_content = self.serialize(request_mapper,  provision_fabric_description)
      request_content = request_content != nil ? JSON.generate(request_content, quirks_mode: true) : nil

      path_template = '$/Provision'

      request_url = @base_url || self.base_url

      options = {
          middlewares: [[MsRest::RetryPolicyMiddleware, times: 3, retry: 0.02], [:cookie_jar]],
          query_params: {'api-version' => api_version,'timeout' => timeout},
          body: request_content,
          headers: request_headers.merge(custom_headers || {}),
          base_url: request_url
      }
      promise = self.make_request_async(:post, path_template, options)

      promise = promise.then do |result|
        http_response = result.response
        status_code = http_response.status
        response_content = http_response.body
        unless status_code == 200
          error_model = JSON.load(response_content)
          fail MsRest::HttpOperationError.new(result.request, http_response, error_model)
        end

        result.request_id = http_response['x-ms-request-id'] unless http_response['x-ms-request-id'].nil?

        result
      end

      promise.execute
    end