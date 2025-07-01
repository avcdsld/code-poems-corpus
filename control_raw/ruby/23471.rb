def call(user:, password:, current_user: nil)
      set_ivars(user, password, current_user)
      validate_call_params
      Success(user: user)
    rescue LogicError => error
      Failure(code: error.message.to_sym)
    end