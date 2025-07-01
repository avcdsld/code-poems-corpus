def to_s
      flags  = 0
      flags |= FLAG_COMPRESSED if compressed?
      flags |= FLAG_IV if iv
      flags |= FLAG_KEY if key
      flags |= FLAG_CIPHER_NAME if cipher_name
      flags |= FLAG_AUTH_TAG if auth_tag

      header = "#{MAGIC_HEADER}#{version.chr(SymmetricEncryption::BINARY_ENCODING)}#{flags.chr(SymmetricEncryption::BINARY_ENCODING)}"

      if iv
        header << [iv.length].pack('v')
        header << iv
      end

      if key
        encrypted = cipher.binary_encrypt(key, header: false)
        header << [encrypted.length].pack('v')
        header << encrypted
      end

      if cipher_name
        header << [cipher_name.length].pack('v')
        header << cipher_name
      end

      if auth_tag
        header << [auth_tag.length].pack('v')
        header << auth_tag
      end

      header
    end