def unchanged?(other)
      unless other.is_a?(self.class)
        raise(ArgumentError, "Can't compare `#{self.class}' with `#{other.class}'")
      end

      equal?(other) ||
      parsers.size == other.parsers.size && all_in_parallel?(parsers, other.parsers) { |one, two| one.unchanged?(two) }
    end