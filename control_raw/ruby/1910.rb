def modify_attribute(options = {})
      options = options.merge(vpc_id: @id)
      resp = @client.modify_vpc_attribute(options)
      resp.data
    end