def modify_embed(enabled, channel, reason = nil)
      cache_embed_data if @embed_enabled.nil?
      channel_id = channel ? channel.resolve_id : @embed_channel_id
      response = JSON.parse(API::Server.modify_embed(@bot.token, @id, enabled, channel_id, reason))
      @embed_enabled = response['enabled']
      @embed_channel_id = response['channel_id']
    end