def initiate_multipart_upload(options = {})
      options = options.merge(
        vault_name: @name,
        account_id: @account_id
      )
      resp = @client.initiate_multipart_upload(options)
      MultipartUpload.new(
        id: resp.data.upload_id,
        account_id: @account_id,
        vault_name: @name,
        client: @client
      )
    end