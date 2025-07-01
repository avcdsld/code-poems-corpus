def headers
      headers = {}
      headers['Content-Type'] = 'application/octet-stream'
      headers['Ttl']          = ttl
      headers['Urgency']      = urgency

      if @payload.key?(:server_public_key)
        headers['Content-Encoding'] = 'aesgcm'
        headers['Encryption'] = "salt=#{salt_param}"
        headers['Crypto-Key'] = "dh=#{dh_param}"
      end

      if api_key?
        headers['Authorization'] = "key=#{api_key}"
      elsif vapid?
        vapid_headers = build_vapid_headers
        headers['Authorization'] = vapid_headers['Authorization']
        headers['Crypto-Key'] = [headers['Crypto-Key'], vapid_headers['Crypto-Key']].compact.join(';')
      end

      headers
    end