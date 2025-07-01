def list(*args)
      arguments(args)
      params = arguments.params
      token = args.shift

      if token.is_a?(Hash) && !params['token'].nil?
        token = params.delete('token')
      elsif token.nil?
        token = oauth_token
      end

      if token.nil?
        raise ArgumentError, 'Access token required'
      end

      headers = { 'Authorization' => "token #{token}" }
      params['headers'] = headers
      response = get_request("/user", params)
      response.headers.oauth_scopes.split(',').map(&:strip)
    end