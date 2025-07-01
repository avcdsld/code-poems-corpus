def create(options = {})
      options = options.merge(group_name: @name)
      resp = @client.create_group(options)
      Group.new(
        name: options[:group_name],
        data: resp.data.group,
        client: @client
      )
    end