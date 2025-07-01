def parse_subpattern(pattern)
      return ISO8601::Duration.new(pattern) if pattern.start_with?('P')

      ISO8601::DateTime.new(pattern)
    end