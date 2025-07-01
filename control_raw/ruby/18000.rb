def live_feed(game_id, timecode: nil)
      MLBStatsAPI::LiveFeed.new(
        self,
        get("/game/#{game_id}/feed/live", version: '1.1', timecode: timecode)
      )
    end