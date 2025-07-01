def https(nsc, timeout = nil)
      http = Net::HTTP.new(nsc.host, nsc.port)
      http.read_timeout = (timeout || nsc.timeout)
      http.open_timeout = nsc.open_timeout
      http.use_ssl = true
      if nsc.trust_store.nil?
        http.verify_mode = OpenSSL::SSL::VERIFY_NONE
      else
        http.cert_store = nsc.trust_store
      end
      http
    end