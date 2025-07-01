def priority=(val)
      no_cmd = (val == default_priority) ? 'no' : ''
      pri = (val == default_priority) ? '' : val
      config_set('interface_ospf', 'priority',
                 @interface.name, no_cmd, pri)
    end