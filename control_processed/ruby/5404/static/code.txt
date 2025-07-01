def enumerate_occurrences(opening_time, closing_time = nil, options = {})
      opening_time = TimeUtil.match_zone(opening_time, start_time)
      closing_time = TimeUtil.match_zone(closing_time, start_time)
      opening_time += TimeUtil.subsec(start_time) - TimeUtil.subsec(opening_time)
      opening_time = start_time if opening_time < start_time
      spans = options[:spans] == true && duration != 0
      Enumerator.new do |yielder|
        reset
        t1 = full_required? ? start_time : opening_time
        t1 -= duration if spans
        t1 = start_time if t1 < start_time
        loop do
          break unless (t0 = next_time(t1, closing_time))
          break if closing_time && t0 > closing_time
          if (spans ? (t0.end_time > opening_time) : (t0 >= opening_time))
            yielder << (block_given? ? yield(t0) : t0)
          end
          t1 = t0 + 1
        end
      end
    end