def set_at positions, val
      validate_positions(*positions)
      positions.map { |pos| @data[pos] = val }
      update_position_cache
    end