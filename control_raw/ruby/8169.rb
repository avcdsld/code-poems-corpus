def recognize_text_async(url, detect_handwriting:false, custom_headers:nil)
      fail ArgumentError, 'azure_region is nil' if azure_region.nil?
      fail ArgumentError, 'url is nil' if url.nil?

      image_url = ImageUrl.new
      unless url.nil?
        image_url.url = url
      end

      request_headers = {}
      request_headers['Content-Type'] = 'application/json; charset=utf-8'

      # Set Headers
      request_headers['x-ms-client-request-id'] = SecureRandom.uuid
      request_headers['accept-language'] = accept_language unless accept_language.nil?

      # Serialize Request
      request_mapper = Azure::CognitiveServices::ComputerVision::V1_0::Models::ImageUrl.mapper()
      request_content = self.serialize(request_mapper,  image_url)
      request_content = request_content != nil ? JSON.generate(request_content, quirks_mode: true) : nil

      path_template = 'recognizeText'

      request_url = @base_url || self.base_url
    request_url = request_url.gsub('{AzureRegion}', azure_region)

      options = {
          middlewares: [[MsRest::RetryPolicyMiddleware, times: 3, retry: 0.02], [:cookie_jar]],
          query_params: {'detectHandwriting' => detect_handwriting},
          body: request_content,
          headers: request_headers.merge(custom_headers || {}),
          base_url: request_url
      }
      promise = self.make_request_async(:post, path_template, options)

      promise = promise.then do |result|
        http_response = result.response
        status_code = http_response.status
        response_content = http_response.body
        unless status_code == 202
          error_model = JSON.load(response_content)
          fail MsRest::HttpOperationError.new(result.request, http_response, error_model)
        end

        result.request_id = http_response['x-ms-request-id'] unless http_response['x-ms-request-id'].nil?

        result
      end

      promise.execute
    end