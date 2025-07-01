def converted_value(other_unit)
      if other_unit.special?
        other_unit.magnitude scalar
      else
        scalar / other_unit.scalar
      end
    end