def authorize user
      auth_conv = HaystackRuby::Auth::Scram::Conversation.new(user, @url)
      auth_conv.authorize
      @auth_token = auth_conv.auth_token
      raise HaystackRuby::Error, "scram authorization failed" unless @auth_token.present?
    end