def update(options = {})
      options = options.merge(user_name: @user_name)
      resp = @client.update_login_profile(options)
      resp.data
    end