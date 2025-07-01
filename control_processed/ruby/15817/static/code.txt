def create(session_id, options = {})
      raise ArgumentError, "session_id not provided" if session_id.to_s.empty?
      raise ArgumentError, "options cannot be empty" if options.empty?
      broadcast_json = @client.start_broadcast(session_id, options)
      Broadcast.new self, broadcast_json
    end