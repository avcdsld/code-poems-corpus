def describe_attribute(options = {})
      options = options.merge(snapshot_id: @id)
      resp = @client.describe_snapshot_attribute(options)
      resp.data
    end