def domain=(d)
      d = d.to_s
      fail ArgumentError unless d.length.between?(1, MAX_VTP_DOMAIN_NAME_SIZE)
      config_set('vtp', 'domain', domain: d)
    end