def include?(tod)
      second = tod.to_i
      second += TimeOfDay::NUM_SECONDS_IN_DAY if second < @range.first
      @range.cover?(second)
    end