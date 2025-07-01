def valid_token?
      uri = URI.join(Teambition::API_DOMAIN, "/api/applications/#{Teambition.client_key}/tokens/check")

      req = Net::HTTP::Get.new(uri)
      req['Authorization'] = "OAuth2 #{token}"

      res = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) do |https|
        https.request(req)
      end
      res.code == '200'
    end