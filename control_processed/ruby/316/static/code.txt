def transition_running_state(target_state)
      state_transitions = {
        not_started: :running,
        running: :stopping,
        stopping: :stopped
      }
      if state_transitions[@running_state] == target_state
        @running_state = target_state
      else
        fail "Bad server state transition: #{@running_state}->#{target_state}"
      end
    end