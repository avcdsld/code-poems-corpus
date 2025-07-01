def filename=(uri)
      fail TypeError if uri.nil?
      Feature.vtp_enable
      uri = uri.to_s
      state = uri.empty? ? 'no' : ''
      config_set('vtp', 'filename', state: state, uri: uri)
    end