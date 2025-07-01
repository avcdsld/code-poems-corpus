def request(uri, data=nil, verb=:post)
      @logger.info(uri) if @logger
      auth_check
      query = {
        path: File.join('v1.0/me/', URI.escape(uri)),
        headers: {
          'Authorization': "Bearer #{@access_token.token}"
        }
      }
      if data
        query[:body] = JSON.generate(data)
        query[:headers]['Content-Type'] = 'application/json'
        @logger.info(query[:body]) if @logger
        verb = :post unless [:post, :put, :patch, :delete].include?(verb)
        response = @conn.send(verb, query)
      else
        response = @conn.get(query)
      end
      JSON.parse(response.body)
    end