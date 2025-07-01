def search_folder_for_envelopes(options={})
      content_type = { 'Content-Type' => 'application/json' }
      content_type.merge(options[:headers]) if options[:headers]

      q ||= []
      options[:query_params].each do |key, val|
        q << "#{key}=#{val}"
      end

      uri = build_uri("/accounts/#{@acct_id}/folders/#{options[:folder_id]}/?#{q.join('&')}")

      http = initialize_net_http_ssl(uri)
      request = Net::HTTP::Get.new(uri.request_uri, headers(content_type))
      response = http.request(request)
      generate_log(request, response, uri)
      JSON.parse(response.body)
    end