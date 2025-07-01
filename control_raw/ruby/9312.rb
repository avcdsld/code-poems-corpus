def search_async(query, accept_language:nil, user_agent:nil, client_id:nil, client_ip:nil, location:nil, country_code:nil, count:nil, freshness:nil, id:nil, length:nil, market:nil, offset:nil, pricing:nil, resolution:nil, safe_search:nil, set_lang:nil, text_decorations:nil, text_format:nil, custom_headers:nil)
      fail ArgumentError, '@client.endpoint is nil' if @client.endpoint.nil?
      x_bing_apis_sdk = 'true'
      fail ArgumentError, 'query is nil' if query.nil?


      request_headers = {}
      request_headers['Content-Type'] = 'application/json; charset=utf-8'

      # Set Headers
      request_headers['x-ms-client-request-id'] = SecureRandom.uuid
      request_headers['X-BingApis-SDK'] = x_bing_apis_sdk unless x_bing_apis_sdk.nil?
      request_headers['Accept-Language'] = accept_language unless accept_language.nil?
      request_headers['User-Agent'] = user_agent unless user_agent.nil?
      request_headers['X-MSEdge-ClientID'] = client_id unless client_id.nil?
      request_headers['X-MSEdge-ClientIP'] = client_ip unless client_ip.nil?
      request_headers['X-Search-Location'] = location unless location.nil?
      path_template = 'videos/search'

      request_url = @base_url || @client.base_url
    request_url = request_url.gsub('{Endpoint}', @client.endpoint)

      options = {
          middlewares: [[MsRest::RetryPolicyMiddleware, times: 3, retry: 0.02], [:cookie_jar]],
          query_params: {'cc' => country_code,'count' => count,'freshness' => freshness,'id' => id,'length' => length,'mkt' => market,'offset' => offset,'pricing' => pricing,'q' => query,'resolution' => resolution,'safeSearch' => safe_search,'setLang' => set_lang,'textDecorations' => text_decorations,'textFormat' => text_format},
          headers: request_headers.merge(custom_headers || {}),
          base_url: request_url
      }
      promise = @client.make_request_async(:get, path_template, options)

      promise = promise.then do |result|
        http_response = result.response
        status_code = http_response.status
        response_content = http_response.body
        unless status_code == 200
          error_model = JSON.load(response_content)
          fail MsRest::HttpOperationError.new(result.request, http_response, error_model)
        end

        result.request_id = http_response['x-ms-request-id'] unless http_response['x-ms-request-id'].nil?
        # Deserialize Response
        if status_code == 200
          begin
            parsed_response = response_content.to_s.empty? ? nil : JSON.load(response_content)
            result_mapper = Azure::CognitiveServices::VideoSearch::V1_0::Models::Videos.mapper()
            result.body = @client.deserialize(result_mapper, parsed_response)
          rescue Exception => e
            fail MsRest::DeserializationError.new('Error occurred in deserializing the response', e.message, e.backtrace, result)
          end
        end

        result
      end

      promise.execute
    end