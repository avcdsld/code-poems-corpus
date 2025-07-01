def update(lead)
      validate_type!(lead)
      params = extract_params!(lead, :id)
      id = params[:id]

      attributes = sanitize(lead)
      _, _, root = @client.put("/leads/#{id}", attributes)

      Lead.new(root[:data])
    end