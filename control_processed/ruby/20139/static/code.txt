def daemon_address=(v)
      v = ENV[DaemonConfig::DAEMON_ADDRESS_KEY] || v
      config = DaemonConfig.new(addr: v)
      emitter.daemon_config = config
      sampler.daemon_config = config if sampler.respond_to?(:daemon_config=)
    end