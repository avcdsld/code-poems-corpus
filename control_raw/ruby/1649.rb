def update(options = {})
      options = options.merge(user_name: @name)
      resp = @client.update_user(options)
      User.new(
        name: options[:new_user_name],
        client: @client
      )
    end