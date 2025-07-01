def create(options = {})
      headers = extract_headers!(options)
      json = client.post("/v1/auth/token/create", JSON.fast_generate(options), headers)
      return Secret.decode(json)
    end