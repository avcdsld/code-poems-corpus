def config_changed?(name)
      logger.debug "config_changed?(#{name.inspect})"
      name = name.to_s
      !(self.cache_files[name] === get_config_files(name))
    end