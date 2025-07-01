def connect_client(ws)
      actor = Actor.current

      # run the blocking websocket client connect+read in a separate thread
      defer {
        # blocks until open, raises on errors
        ws.connect

        # These are called from the read_ws -> defer thread, proxy back to actor
        actor.on_open

        ws.read do |message|
          actor.on_message(message)
        end
      }

    rescue Kontena::Websocket::CloseError => exc
      # handle known errors, will reconnect
      on_close(exc.code, exc.reason)

    rescue Kontena::Websocket::Error => exc
      # handle known errors, will reconnect
      on_close(1006, exc.message)

    rescue => exc
      # TODO: crash instead of reconnecting on unknown errors?
      error exc
      on_close(1006, exc.message)

    else
      # client closed, not going to happen
      on_close(ws.close_code, ws.close_reason)

    ensure
      @ws = nil

      ws.disconnect
    end