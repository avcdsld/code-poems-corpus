def get_unit(key)
    @counters[key] ||= 0
    @counters[key] += @interval
    @counters[key] = @counters[key] - 1.0 if @counters[key] > 1
    @counters[key] = @counters[key] + 1.0 if @counters[key] < 0
    @counters[key]
  end