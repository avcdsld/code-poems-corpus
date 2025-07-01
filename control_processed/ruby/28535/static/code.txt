def parse_time(time, in_ms = false)
      return relative_time(time, in_ms) if time =~ /^[\-+]/
      ParseTime.new(time, in_ms).parse!
    end