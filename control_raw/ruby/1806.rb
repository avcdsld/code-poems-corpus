def create_network_acl(options = {})
      resp = @client.create_network_acl(options)
      NetworkAcl.new(
        id: resp.data.network_acl.network_acl_id,
        data: resp.data.network_acl,
        client: @client
      )
    end