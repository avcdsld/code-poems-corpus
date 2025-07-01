def delete(options = {})
      options = options.merge(
        auto_scaling_group_name: @group_name,
        topic_arn: @topic_arn
      )
      resp = @client.delete_notification_configuration(options)
      resp.data
    end