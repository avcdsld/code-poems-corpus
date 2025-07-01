def valid_representation?(date, time)
      year, month, day = date
      hour = time.first

      date.nil? || !(!year.nil? && (month.nil? || day.nil?) && !hour.nil?)
    end