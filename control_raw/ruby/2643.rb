def token(new_token)
      old_token    = client.token
      client.token = new_token
      json = client.get("/v1/auth/token/lookup-self")
      secret = Secret.decode(json)
      return secret
    rescue
      client.token = old_token
      raise
    end