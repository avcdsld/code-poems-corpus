def allow( event )
    return nil if @level > event.level
    @filters.each do |filter|
      break unless event = filter.allow(event)
    end
    event
  end