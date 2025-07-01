def previous_occurrences(num, from)
      from = TimeUtil.match_zone(from, start_time) or raise ArgumentError, "Time required, got #{from.inspect}"
      return [] if from <= start_time
      a = enumerate_occurrences(start_time, from - 1).to_a
      a.size > num ? a[-1*num,a.size] : a
    end