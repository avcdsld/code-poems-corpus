def put(options = {})
      options = options.merge(
        bucket: @bucket_name,
        key: @object_key
      )
      resp = @client.put_object_acl(options)
      resp.data
    end