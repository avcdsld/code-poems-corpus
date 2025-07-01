def delete(options = {})
      options = options.merge(endpoint_arn: @arn)
      resp = @client.delete_endpoint(options)
      resp.data
    end