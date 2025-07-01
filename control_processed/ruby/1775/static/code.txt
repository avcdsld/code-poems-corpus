def delete(options = {})
      options = options.merge(launch_configuration_name: @name)
      resp = @client.delete_launch_configuration(options)
      resp.data
    end