def find_cipher_key(*args)
      fail ArgumentError, 'Unknown key derivation name ', args[1] unless args[1] == 'PBKDF2'

      ::OpenSSL::PKCS5.pbkdf2_hmac_sha1(args[2], args[3], args[4], args[0].key_len)
    end