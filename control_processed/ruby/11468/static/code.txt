def every(field)
      @lines.reduce([]) { |result, fields| result << fields[field] if fields.key?(field); result }
    end