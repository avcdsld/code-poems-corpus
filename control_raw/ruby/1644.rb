def create_policy(options = {})
      options = options.merge(user_name: @name)
      resp = @client.put_user_policy(options)
      UserPolicy.new(
        user_name: @name,
        name: options[:policy_name],
        client: @client
      )
    end