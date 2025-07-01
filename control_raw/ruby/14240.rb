def process(data)
      message = MultiJson.load(data, symbolize_keys: true)
      event   = message[:event]

      PusherFake.log("RECV #{id}: #{message}")

      if event.start_with?(CLIENT_EVENT_PREFIX)
        process_trigger(event, message)
      else
        process_event(event, message)
      end
    end