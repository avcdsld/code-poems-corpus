def revoke_egress(options = {})
      options = options.merge(group_id: @id)
      resp = @client.revoke_security_group_egress(options)
      resp.data
    end