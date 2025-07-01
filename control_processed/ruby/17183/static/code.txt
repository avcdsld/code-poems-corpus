def to_units(*units)
      sorted_units = self.class.sort_units(units).reverse

      _, parts = sorted_units.reduce([self, {}]) do |(remainder, parts), unit|
        part = remainder.to_unit(unit)
        new_remainder = remainder - Duration.new(unit => part)

        [new_remainder, parts.merge(unit => part)]
      end

      parts
    end