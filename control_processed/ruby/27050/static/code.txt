def quietly(*args, &block)
      previous_state = @rye_quiet
      enable_quiet_mode
      ret = self.instance_exec *args, &block
      @rye_quiet = previous_state
      ret
    end