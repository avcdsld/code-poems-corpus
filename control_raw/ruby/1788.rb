def add_permission(options = {})
      options = options.merge(topic_arn: @arn)
      resp = @client.add_permission(options)
      resp.data
    end