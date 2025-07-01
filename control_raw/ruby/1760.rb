def modify_attribute(options = {})
      options = options.merge(instance_id: @id)
      resp = @client.modify_instance_attribute(options)
      resp.data
    end