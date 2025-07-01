def create(deal)
      validate_type!(deal)

      attributes = sanitize(deal)
      _, _, root = @client.post("/deals", attributes)

      Deal.new(root[:data])
    end