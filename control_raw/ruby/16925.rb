def digest_auth(user, password)
      builder.insert(0, Faraday::Request::DigestAuth, user, password)
    end