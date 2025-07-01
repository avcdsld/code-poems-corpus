def next(pointer)
      super

      unless @current_week_start
        case pointer
        when :future
          saturday_repeater = RepeaterDayName.new(:saturday)
          saturday_repeater.start = @now
          next_saturday_span = saturday_repeater.next(:future)
          @current_week_start = next_saturday_span.begin
        when :past
          saturday_repeater = RepeaterDayName.new(:saturday)
          saturday_repeater.start = (@now + RepeaterDay::DAY_SECONDS)
          last_saturday_span = saturday_repeater.next(:past)
          @current_week_start = last_saturday_span.begin
        end
      else
        direction = pointer == :future ? 1 : -1
        @current_week_start += direction * RepeaterWeek::WEEK_SECONDS
      end

      Span.new(@current_week_start, @current_week_start + WEEKEND_SECONDS)
    end