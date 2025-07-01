def shutdown(exit_event = ExitEvent.new(behavior_proxy))
      @behavior.shutdown
      cleanup exit_event
    ensure
      Thread.current[:celluloid_actor]   = nil
      Thread.current[:celluloid_mailbox] = nil
    end