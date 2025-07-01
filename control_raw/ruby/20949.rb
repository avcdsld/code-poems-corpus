def create(tag)
      validate_type!(tag)

      attributes = sanitize(tag)
      _, _, root = @client.post("/tags", attributes)

      Tag.new(root[:data])
    end