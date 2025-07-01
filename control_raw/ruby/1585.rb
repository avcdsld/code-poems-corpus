def delete(options = {})
      options = options.merge(db_parameter_group_name: @name)
      resp = @client.delete_db_parameter_group(options)
      resp.data
    end