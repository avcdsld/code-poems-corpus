def hour(system = :twenty_four_hour)
      hour = self.to_duration.to_units(:hour, :minute, :second).fetch(:hour)
      if system == :twelve_hour
        if hour == 0
          12
        elsif hour > 12
          hour - 12
        else
          hour
        end
      elsif (system == :twenty_four_hour)
        hour
      else
        raise ArgumentError, "system should be :twelve_hour or :twenty_four_hour"
      end
    end