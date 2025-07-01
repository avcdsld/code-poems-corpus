def attach_classic_link_instance(options = {})
      options = options.merge(vpc_id: @id)
      resp = @client.attach_classic_link_vpc(options)
      resp.data
    end