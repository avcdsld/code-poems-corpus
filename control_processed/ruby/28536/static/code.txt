def relative_time(time, in_ms = false, ref = Time.now)
      ref = in_ms ? ref.to_datetime.strftime('%Q') : ref.to_time
      ref.to_i + parse_relative_time(time, in_ms)
    end