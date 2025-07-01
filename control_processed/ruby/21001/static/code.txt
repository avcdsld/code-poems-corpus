def atomize(input)
      _, time, zone = parse_timezone(input)
      _, hour, separator, minute, second = parse_time(time)

      raise(ISO8601::Errors::UnknownPattern, @original) if hour.nil?

      @separator = separator
      require_separator = require_separator(minute)

      hour = hour.to_i
      minute = minute.to_i
      second = parse_second(second)

      atoms = [hour, minute, second, zone].compact

      raise(ISO8601::Errors::UnknownPattern, @original) unless valid_zone?(zone, require_separator)

      atoms
    end