def display_error_message(ex) # :nodoc:
      trace "#{name} aborted!"
      display_exception_details(ex)
      trace "Tasks: #{ex.chain}" if has_chain?(ex)
      trace "(See full trace by running task with --trace)" unless
         options.backtrace
    end