def reset_password user, password
      Oath.config.password_reset_service.new(user, password).perform
    end