def compare_small_comparators(other)
      return true if @size > SMALL_FILE || other.size > SMALL_FILE
      return true if small_comparator.nil? || other.small_comparator.nil?

      small_comparator.call == other.small_comparator.call
    end