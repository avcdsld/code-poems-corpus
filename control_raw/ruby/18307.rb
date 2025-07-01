def put_xml(path, credentials, data)
      full_url = PagSeguro.api_url("#{path}?#{credentials_to_params(credentials)}")

      request.put do
        url full_url
        headers "Content-Type" => "application/xml; charset=#{PagSeguro.encoding}",
                "Accept" => "application/vnd.pagseguro.com.br.v1+xml;charset=ISO-8859-1"
        body data
      end
    end