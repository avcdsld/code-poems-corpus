def initiate_multipart_upload(options = {})
      options = options.merge(
        bucket: @bucket_name,
        key: @key
      )
      resp = @client.create_multipart_upload(options)
      MultipartUpload.new(
        bucket_name: @bucket_name,
        object_key: @key,
        id: resp.data.upload_id,
        client: @client
      )
    end