def access_token(code)
      response = connection.post("/api/oauth/token",
        client_id:     client_id,
        client_secret: client_secret,
        code:          code,
        redirect_uri:  redirect_uri,
        grant_type:    "authorization_code"
      )

      if response.success?
        OpenStruct.new(response.body)
      else
        raise Error.new(response.body["error_description"])
      end
    end