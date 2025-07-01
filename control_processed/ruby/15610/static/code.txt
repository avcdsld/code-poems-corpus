def can?(*args)
      event_name  = args.shift
      events_map.can_perform?(event_name, current, *args)
    end