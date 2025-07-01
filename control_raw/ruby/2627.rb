def enable_auth(path, type, description = nil)
      payload = { type: type }
      payload[:description] = description if !description.nil?

      client.post("/v1/sys/auth/#{encode_path(path)}", JSON.fast_generate(payload))
      return true
    end