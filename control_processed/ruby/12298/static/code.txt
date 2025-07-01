def replace_values old_values, new_value
      old_values = [old_values] unless old_values.is_a? Array
      rename_hash = old_values.map { |v| [v, new_value] }.to_h
      rename_categories rename_hash
    end