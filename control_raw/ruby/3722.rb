def array_to_cells(values, options={})
      DataTypeValidator.validate :array_to_cells, Array, values
      types, style, formula_values = options.delete(:types), options.delete(:style), options.delete(:formula_values)
      values.each_with_index do |value, index|
        options[:style] = style.is_a?(Array) ? style[index] : style if style
        options[:type] = types.is_a?(Array) ? types[index] : types if types
        options[:formula_value] = formula_values[index] if formula_values.is_a?(Array)

        self[index] = Cell.new(self, value, options)
      end
    end