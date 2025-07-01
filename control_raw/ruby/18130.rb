def to_seed(mnemonic, passphrase: '')
      to_entropy(mnemonic)
      OpenSSL::PKCS5.pbkdf2_hmac(mnemonic.join(' ').downcase,
                                 'mnemonic' + passphrase, 2048, 64, OpenSSL::Digest::SHA512.new).bth
    end