def parse_id_token(id_token)
      if id_token.nil?
        logger.warn('No id token found.')
        @user_info ||= ADAL::UserInformation.new(unique_id: SecureRandom.uuid)
        return
      end
      logger.verbose('Attempting to decode id token in token response.')
      claims = JWT.decode(id_token.to_s, nil, false).first
      @id_token = id_token
      @user_info = ADAL::UserInformation.new(claims)
    end