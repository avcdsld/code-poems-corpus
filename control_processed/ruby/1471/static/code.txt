def update(options = {})
      options = options.merge(group_name: @name)
      resp = @client.update_group(options)
      Group.new(
        name: options[:new_group_name],
        client: @client
      )
    end