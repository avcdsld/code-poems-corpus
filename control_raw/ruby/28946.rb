def known_machine_group?
      raise NoConfig unless @@config
      return true if default_machine_group?
      raise NoMachinesConfig unless @@config.machines
      return false if !@@config && !@@global
      zon, env, rol = @@global.zone, @@global.environment, @@global.role
      conf = @@config.machines.find_deferred(@@global.region, zon, [env, rol])
      conf ||= @@config.machines.find_deferred(zon, [env, rol])
      !conf.nil?
    end