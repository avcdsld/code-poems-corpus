def initial_state=(new_initial_state)
      @initial_state = new_initial_state
      add_states([@initial_state]) unless dynamic_initial_state?

      # Update all states to reflect the new initial state
      states.each { |state| state.initial = (state.name == @initial_state) }

      # Output a warning if there are conflicting initial states for the machine's
      # attribute
      initial_state = states.detect { |state| state.initial }
      if !owner_class_attribute_default.nil? && (dynamic_initial_state? || !owner_class_attribute_default_matches?(initial_state))
        warn(
            "Both #{owner_class.name} and its #{name.inspect} machine have defined "\
          "a different default for \"#{attribute}\". Use only one or the other for "\
          "defining defaults to avoid unexpected behaviors."
        )
      end
    end