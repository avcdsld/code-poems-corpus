def dates(date_range)
      if date_range.is_a? String

        # assume the user knows what she is doing if passed a string
        @query[:params][:date] = date_range
      elsif date_range.is_a? Range
        start = date_range.first
        last = date_range.last
        @query[:params][:date] = "#{start.strftime("%YM%m")}:#{last.strftime("%YM%m")}"
      end
      self
    end