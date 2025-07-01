def delete(options = {})
      options = options.merge(group_name: @name)
      resp = @client.delete_group(options)
      resp.data
    end