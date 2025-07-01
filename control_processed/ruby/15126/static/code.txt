def verify(app_id)
      # Chapter 4.3 in
      # http://fidoalliance.org/specs/fido-u2f-raw-message-formats-v1.0-rd-20141008.pdf
      data = [
        "\x00",
        ::U2F::DIGEST.digest(app_id),
        ::U2F::DIGEST.digest(client_data_json),
        key_handle_raw,
        public_key_raw
      ].join

      begin
        parsed_certificate.public_key.verify(::U2F::DIGEST.new, signature, data)
      rescue OpenSSL::PKey::PKeyError
        false
      end
    end