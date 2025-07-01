def stop
      Debugger.stop if !@always_enabled && Debugger.started?
      if PryDebugger.current_remote_server   # Cleanup DRb remote if running
        PryDebugger.current_remote_server.teardown
      end
    end