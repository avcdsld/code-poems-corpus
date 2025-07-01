def authorize_ingress(options = {})
      options = options.merge(db_security_group_name: @name)
      resp = @client.authorize_db_security_group_ingress(options)
      DBSecurityGroup.new(
        name: resp.data.db_security_group.db_security_group_name,
        data: resp.data.db_security_group,
        client: @client
      )
    end