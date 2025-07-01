def make_invite(max_age = 0, max_uses = 0, temporary = false, unique = false, reason = nil)
      response = API::Channel.create_invite(@bot.token, @id, max_age, max_uses, temporary, unique, reason)
      Invite.new(JSON.parse(response), @bot)
    end