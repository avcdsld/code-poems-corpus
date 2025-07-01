def change_state_to(state_name, new_state, trigger = true)
      # use an instance variable for the state storage
      ivar_name = :"@#{state_name}"

      old_state = instance_variable_get(ivar_name)
      instance_variable_set(ivar_name, new_state)

      # Trigger changed on the 'state' method
      if old_state != new_state && trigger
        dep = state_dep_for(state_name, false)
        dep.changed! if dep
      end
    end