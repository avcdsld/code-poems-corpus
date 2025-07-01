def provisioning_uri(name, initial_count = 0)
      params = {
        secret: secret,
        counter: initial_count,
        digits: digits == DEFAULT_DIGITS ? nil : digits
      }
      encode_params("otpauth://hotp/#{Addressable::URI.escape(name)}", params)
    end