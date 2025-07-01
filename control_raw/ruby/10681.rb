def sign_request(request)
      super(request)
      encodeCredentials = Base64.strict_encode64("#{user_name}:#{password}")
      credentials = "#{scheme} #{encodeCredentials}"

      if (request.respond_to?(:request_headers))
        request.request_headers[AUTHORIZATION] = credentials
      elsif request.respond_to?(:headers)
        request.headers[AUTHORIZATION] = credentials
      else
        fail ArgumentError, 'Incorrect request object was provided'
      end
    end