def update(options = {})
      options = options.merge(auto_scaling_group_name: @name)
      resp = @client.update_auto_scaling_group(options)
      AutoScalingGroup.new(
        name: options[:auto_scaling_group_name],
        client: @client
      )
    end