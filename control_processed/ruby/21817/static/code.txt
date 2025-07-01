def enable
      value = config_get('snmpnotification', 'enable', trap_name: @name)
      enabled = value.nil? ? false : true
      enabled
    end