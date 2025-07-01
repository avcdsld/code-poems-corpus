def center(intervals)
      i = intervals.reduce([intervals.first.first, intervals.first.last]) { |acc, int| [[acc.first, int.first].min, [acc.last, int.last].max] }
      i.first + (i.last - i.first) / 2
    end