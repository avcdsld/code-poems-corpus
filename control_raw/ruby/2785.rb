def on(event, &proc)
      unless @events.has_key? event
        raise Error, "`#{event}` is not a valid event type"
      end
      event_id = new_event_key
      @events[event][event_id] = proc
      EventDescriptor.new(event, event_id)
    end