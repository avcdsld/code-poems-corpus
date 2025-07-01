def get_async_common(request)
      fail ValidationError, 'Request cannot be nil' if request.nil?

      request.middlewares = [[MsRest::RetryPolicyMiddleware, times: 3, retry: 0.02], [:cookie_jar]]
      request.headers.merge!({'x-ms-client-request-id' => SecureRandom.uuid}) unless request.headers.key?('x-ms-client-request-id')
      request.headers.merge!({'Content-Type' => 'application/json'}) unless request.headers.key?('Content-Type')

      # Send Request
      http_response = request.run_promise do |req|
        @credentials.sign_request(req) unless @credentials.nil?
      end.execute.value!

      status_code = http_response.status

      if status_code != 200 && status_code != 201 && status_code != 202 && status_code != 204
        json_error_data = JSON.load(http_response.body)
        error_data = CloudErrorData.deserialize_object(json_error_data)

        fail AzureOperationError.new request, http_response, error_data, "Long running operation failed with status #{status_code}"
      end

      result = MsRest::HttpOperationResponse.new(request, http_response, http_response.body)

      begin
        result.body = JSON.load(http_response.body) unless http_response.body.to_s.empty?
      rescue Exception => e
        fail MsRest::DeserializationError.new("Error occured in deserializing the response", e.message, e.backtrace, result)
      end

      result
    end