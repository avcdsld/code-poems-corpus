def begin_renew_certificate(fabric_name, renew_certificate, custom_headers:nil)
      response = begin_renew_certificate_async(fabric_name, renew_certificate, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end