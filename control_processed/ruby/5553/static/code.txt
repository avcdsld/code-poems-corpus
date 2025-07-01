def compile_attribute_values(values)
      if values.map(&:key).uniq.size == 1
        compile_attribute(values.first.key, values)
      else
        runtime_build(values)
      end
    end