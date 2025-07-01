def parse_unit_string(unit_string)
      denominator_units = numerator_units = Sass::Script::Value::Number::NO_UNITS
      return numerator_units, denominator_units unless unit_string && unit_string.length > 0
      num_over_denominator = unit_string.split(%r{ */ *})
      unless (1..2).include?(num_over_denominator.size)
        raise ArgumentError.new("Malformed unit string: #{unit_string}")
      end
      numerator_units = num_over_denominator[0].split(/ *\* */)
      denominator_units = (num_over_denominator[1] || "").split(/ *\* */)
      [[numerator_units, "numerator"], [denominator_units, "denominator"]].each do |units, name|
        if unit_string =~ %r{/} && units.size == 0
          raise ArgumentError.new("Malformed unit string: #{unit_string}")
        end
        if units.any? {|unit| unit !~ VALID_UNIT}
          raise ArgumentError.new("Malformed #{name} in unit string: #{unit_string}")
        end
      end
      [numerator_units, denominator_units]
    end