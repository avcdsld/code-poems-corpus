def verify(content, signature)
      hmac = OpenSSL::HMAC.hexdigest('sha1', @secret, content)
      signature.downcase == "sha1=#{hmac}"
    end