def global_service_command_permitted(sv_cmd, service_name)
      # For services that have been removed, we only want to
      # them to respond to the stop command. They should not show
      # up in status, and they should not be started.
      if removed_services.include?(service_name)
        return sv_cmd == "stop"
      end

      # For keepalived, we only want it to respond to the status
      # command when running global service commands like p-c-c start
      # and p-c-c stop
      if service_name == "keepalived"
        return sv_cmd == "status"
      end

      # If c-s-c status is called, check to see if the service
      # is hidden supposed to be hidden from the status results
      # (mover for example should be hidden).
      if sv_cmd == "status"
        return !(hidden_services.include?(service_name))
      end

      # All other services respond normally to p-c-c * commands
      return true
    end