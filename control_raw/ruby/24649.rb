def rfc6979_ecdsa_nonce(hash, privkey)
      raise ArgumentError, "Hash must be 32 bytes long" if hash.bytesize != 32
      raise ArgumentError, "Private key must be 32 bytes long" if privkey.bytesize != 32

      autorelease do |pool|
        order = self.group_order

        # Step 3.2.a. hash = H(message). Already performed by the caller.

        # Step 3.2.b. V = 0x01 0x01 0x01 ... 0x01 (32 bytes equal 0x01)
        v = "\x01".b*32

        # Step 3.2.c. K = 0x00 0x00 0x00 ... 0x00 (32 bytes equal 0x00)
        k = "\x00".b*32

        # Step 3.2.d. K = HMAC-SHA256(key: K, data: V || 0x00 || int2octets(privkey) || bits2octets(hash))
        h1 = pool.new_bn(hash)
        BN_div(nil, h1, h1, order, pool.bn_ctx) # h1 = h1 % order
        h1data = data_from_bn(h1, min_length: 32)
        k = BTC.hmac_sha256(key: k, data: v + "\x00".b + privkey + h1data)

        # Step 3.2.e. V = HMAC-SHA256(key: K, data: V)
        v = BTC.hmac_sha256(key: k, data: v)

        # Step 3.2.f. K = HMAC-SHA256(key: K, data: V || 0x01 || int2octets(privkey) || bits2octets(hash))
        k = BTC.hmac_sha256(key: k, data: v + "\x01".b + privkey + h1data)

        # Step 3.2.g. V = HMAC-SHA256(key: K, data: V)
        v = BTC.hmac_sha256(key: k, data: v)

        # Step 3.2.h.
        zero32 = "\x00".b*32
        10000.times do
          t = BTC.hmac_sha256(key: k, data: v)
          tn = pool.new_bn(t)
          if BN_cmp(tn, order) < 0
            nonce = data_from_bn(tn, min_length: 32)
            if nonce != zero32
              return nonce
            end
          end
          # Note: the probability of not succeeding at the first try is about 2^-127.
          k = BTC.hmac_sha256(key: k, data: v + zero32)
          v = BTC.hmac_sha256(key: k, data: v)
        end
        # we generated 10000 numbers, none of them is good -> fail.
        raise "Cannot find any good ECDSA nonce after 10000 iterations of RFC6979."
      end
    end