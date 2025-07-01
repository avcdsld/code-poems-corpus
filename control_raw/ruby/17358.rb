def scoped_timeline(ids, opts = {})
      ids      = ids.join(',') if ids.is_a?(Array)
      params   = { user_ids: ids }.merge!(opts)
      resource = SCOPED_TIMELINE % { id: @id }
      request  = Request.new(client, :get, resource, params: params)
      response = request.perform
      response.body[:data]
    end