def request(req)
      json_str = JSON::generate(req, { :ascii_only=>true })
      http    = Net::HTTP.new(@uri.host, @uri.port)
      request = Net::HTTP::Post.new(@uri.request_uri)
      request.body = json_str
      request["Content-Type"] = "application/json"
      response = http.request(request)
      if response.code != "200"
        raise RpcException.new(-32000, "Non-200 response #{response.code} from #{@url}")
      else
        return JSON::parse(response.body)
      end
    end