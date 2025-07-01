def ban(user, message_days = 0, reason: nil)
      API::Server.ban_user(@bot.token, @id, user.resolve_id, message_days, reason)
    end