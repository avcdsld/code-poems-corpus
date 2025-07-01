def main_loop
      debug("Entering request handler main loop")
      reset_signal_handlers
      begin
        @graceful_termination_pipe = IO.pipe
        @graceful_termination_pipe[0].close_on_exec!
        @graceful_termination_pipe[1].close_on_exec!

        @main_loop_thread_lock.synchronize do
          @main_loop_generation += 1
          @main_loop_running = true
          @main_loop_thread_cond.broadcast

          @select_timeout = nil

          @selectable_sockets = []
          @server_sockets.each_value do |value|
            socket = value[2]
            @selectable_sockets << socket if socket
          end
          @selectable_sockets << @owner_pipe
          @selectable_sockets << @graceful_termination_pipe[0]
        end

        install_useful_signal_handlers
        start_threads
        wait_until_termination_requested
        wait_until_all_threads_are_idle
        terminate_threads
        debug("Request handler main loop exited normally")

      rescue EOFError
        # Exit main loop.
        trace(2, "Request handler main loop interrupted by EOFError exception")
      rescue Interrupt
        # Exit main loop.
        trace(2, "Request handler main loop interrupted by Interrupt exception")
      rescue SignalException => signal
        trace(2, "Request handler main loop interrupted by SignalException")
        if signal.message != HARD_TERMINATION_SIGNAL
          raise
        end
      rescue Exception => e
        trace(2, "Request handler main loop interrupted by #{e.class} exception")
        raise
      ensure
        debug("Exiting request handler main loop")
        revert_signal_handlers
        @main_loop_thread_lock.synchronize do
          @graceful_termination_pipe[1].close rescue nil
          @graceful_termination_pipe[0].close rescue nil
          @selectable_sockets = []
          @main_loop_generation += 1
          @main_loop_running = false
          @main_loop_thread_cond.broadcast
        end
      end
    end