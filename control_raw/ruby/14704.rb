def add_sibling_machine_configs
      # Add existing states
      sibling_machines.each do |machine|
        machine.states.each { |state| states << state unless states[state.name] }
      end
    end