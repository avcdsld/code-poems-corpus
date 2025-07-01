def put(options = {})
      options = options.merge(
        group_name: @group_name,
        policy_name: @name
      )
      resp = @client.put_group_policy(options)
      resp.data
    end