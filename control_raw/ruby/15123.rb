def authenticate!(challenge, response, registration_public_key, registration_counter)
      # TODO: check that it's the correct key_handle as well
      raise NoMatchingRequestError unless challenge == response.client_data.challenge

      raise ClientDataTypeError unless response.client_data.authentication?

      pem = U2F.public_key_pem(registration_public_key)

      raise AuthenticationFailedError unless response.verify(app_id, pem)

      raise UserNotPresentError unless response.user_present?

      unless response.counter > registration_counter
        raise CounterTooLowError unless response.counter.zero? && registration_counter.zero?
      end
    end