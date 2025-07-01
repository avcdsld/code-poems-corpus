def at(point, &block)
      # obvious cases first
      if @sorted.empty?
        # no key points
        return nil
      elsif @sorted.size == 1
        # one key point
        return @sorted.first.last
      end

      # out-of-bounds cases next
      if point <= @min_point
        # lower than lowest key point
        return @sorted.first.last
      elsif point >= @max_point
        # higher than highest key point
        return @sorted.last.last
      end

      # binary search to find the right interpolation key point/value interval
      left = 0
      right = @sorted.length - 2 # highest point will be included
      low_point = nil
      low_value = nil
      high_point = nil
      high_value = nil

      while left <= right
        middle = (right - left) / 2 + left

        (low_point, low_value) = @sorted[middle]
        (high_point, high_value) = @sorted[middle + 1]

        break if low_point <= point and point <= high_point

        if point < low_point
          right = middle - 1
        else
          left = middle + 1
        end
      end

      # determine the balance ratio
      span = high_point - low_point
      balance = (point.to_f - low_point) / span

      # choose and call the blending function
      blend = block || @blend_with || DEFAULT_BLEND
      blend.call(low_value, high_value, balance)
    end