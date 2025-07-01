def get_login_information(options={})
      uri = build_uri('/login_information')
      request = Net::HTTP::Get.new(uri.request_uri, headers(options[:headers]))
      http = initialize_net_http_ssl(uri)
      response = http.request(request)
      generate_log(request, response, uri)
      response
    end