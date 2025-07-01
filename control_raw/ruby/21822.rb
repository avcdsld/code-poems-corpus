def bfd=(val)
      return if val == bfd
      Feature.bfd_enable
      state = (val == default_bfd) ? 'no' : ''
      disable = val ? '' : 'disable'
      config_set('interface_ospf', 'bfd', @interface.name,
                 state, disable)
    end