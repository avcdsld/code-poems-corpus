def run
      unless stack_exists?(@stack_name)
        puts "The stack #{@stack_name.color(:green)} does not exist."
        return
      end

      resp = cloudformation.describe_stacks(stack_name: @stack_name)
      stack = resp.stacks.first

      puts "The current status for the stack #{@stack_name.color(:green)} is #{stack.stack_status.color(:green)}"

      status_poller = Stack::Status.new(@stack_name)

      if stack.stack_status =~ /_IN_PROGRESS$/
        puts "Stack events (tailing):"
        # tail all events until done
        status_poller.hide_time_took = true
        status_poller.wait
      else
        puts "Stack events:"
        # show the last events that was user initiated
        status_poller.refresh_events
        status_poller.show_events(true)
      end
    end