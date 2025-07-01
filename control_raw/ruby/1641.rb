def create(options = {})
      options = options.merge(user_name: @name)
      resp = @client.create_user(options)
      User.new(
        name: options[:user_name],
        data: resp.data.user,
        client: @client
      )
    end