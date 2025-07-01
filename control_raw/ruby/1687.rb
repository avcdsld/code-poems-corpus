def modify(options = {})
      options = options.merge(option_group_name: @name)
      resp = @client.modify_option_group(options)
      OptionGroup.new(
        name: resp.data.option_group.option_group_name,
        data: resp.data.option_group,
        client: @client
      )
    end