def decrypt(self, data):
        '''
        verify HMAC-SHA256 signature and decrypt data with AES-CBC
        '''
        aes_key, hmac_key = self.keys
        sig = data[-self.SIG_SIZE:]
        data = data[:-self.SIG_SIZE]
        if six.PY3 and not isinstance(data, bytes):
            data = salt.utils.stringutils.to_bytes(data)
        mac_bytes = hmac.new(hmac_key, data, hashlib.sha256).digest()
        if len(mac_bytes) != len(sig):
            log.debug('Failed to authenticate message')
            raise AuthenticationError('message authentication failed')
        result = 0

        if six.PY2:
            for zipped_x, zipped_y in zip(mac_bytes, sig):
                result |= ord(zipped_x) ^ ord(zipped_y)
        else:
            for zipped_x, zipped_y in zip(mac_bytes, sig):
                result |= zipped_x ^ zipped_y
        if result != 0:
            log.debug('Failed to authenticate message')
            raise AuthenticationError('message authentication failed')
        iv_bytes = data[:self.AES_BLOCK_SIZE]
        data = data[self.AES_BLOCK_SIZE:]
        if HAS_M2:
            cypher = EVP.Cipher(alg='aes_192_cbc', key=aes_key, iv=iv_bytes, op=0, padding=False)
            encr = cypher.update(data)
            data = encr + cypher.final()
        else:
            cypher = AES.new(aes_key, AES.MODE_CBC, iv_bytes)
            data = cypher.decrypt(data)
        if six.PY2:
            return data[:-ord(data[-1])]
        else:
            return data[:-data[-1]]