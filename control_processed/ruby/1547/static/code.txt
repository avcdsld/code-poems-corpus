def put(options = {})
      options = options.merge(bucket: @bucket_name)
      resp = @client.put_bucket_cors(options)
      resp.data
    end