def parsed_time
      return @parsed_time if @parsed_time

      @parsed_time = parsed_day
      change_hour = next_hour

      # There is no hour 24, so we need to move to the next day
      if change_hour == 24
        @parsed_time = 1.day.from_now(@parsed_time)
        change_hour = 0
      end

      @parsed_time = @parsed_time.change(hour: change_hour, min: at_min)

      # If the parsed time is still before the current time, add an additional day if
      # the week day wasn't specified or add an additional week to get the correct time.
      @parsed_time += at_wday? ? 1.week : 1.day if now > @parsed_time
      @parsed_time
    end