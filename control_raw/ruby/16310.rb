def limit_exceeded(amount = 1)
      limits.each do |limit|
        limit_exceeded = limit.limit_exceeded(amount)
        return limit_exceeded if limit_exceeded
      end
      nil
    end