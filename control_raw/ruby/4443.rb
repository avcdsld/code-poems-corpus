def cache_embed_data
      data = JSON.parse(API::Server.embed(@bot.token, @id))
      @embed_enabled = data['enabled']
      @embed_channel_id = data['channel_id']
    end