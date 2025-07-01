def scalar(magnitude = value)
      if special?
        unit.scalar(magnitude)
      else
        Number.rationalize(value) * Number.rationalize(unit.scalar)
      end
    end