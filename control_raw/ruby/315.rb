def stop
      # if called via run_till_terminated_or_interrupted,
      #   signal stop_server_thread and dont do anything
      if @stop_server.nil? == false && @stop_server == false
        @stop_server = true
        @stop_server_cv.broadcast
        return
      end
      @run_mutex.synchronize do
        fail 'Cannot stop before starting' if @running_state == :not_started
        return if @running_state != :running
        transition_running_state(:stopping)
        deadline = from_relative_time(@poll_period)
        @server.shutdown_and_notify(deadline)
      end
      @pool.stop
    end