def set_at positions, val
      validate_positions(*positions)
      positions.map { |pos| modify_category_at pos, val }
      self
    end