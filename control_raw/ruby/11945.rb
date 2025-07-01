def prepare_locals(params)
      locals = params.delete(:locals) || {}
      prepared_parameters = prepare_parameters(params)
      locals.merge\
        notification: self,
        controller:   ActivityNotification.get_controller,
        parameters:   prepared_parameters
    end