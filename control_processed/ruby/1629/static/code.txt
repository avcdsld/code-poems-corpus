def update(options = {})
      options = options.merge(server_certificate_name: @name)
      resp = @client.update_server_certificate(options)
      ServerCertificate.new(
        name: options[:new_server_certificate_name],
        client: @client
      )
    end