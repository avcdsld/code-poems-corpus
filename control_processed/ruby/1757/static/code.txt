def describe_attribute(options = {})
      options = options.merge(instance_id: @id)
      resp = @client.describe_instance_attribute(options)
      resp.data
    end