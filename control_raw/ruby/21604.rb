def key_match?(type, keys, doc)

      _id = doc.is_a?(Hash) ? doc['_id'] : doc

      if keys.first.is_a?(String) && type == 'schedules'
        keys.find { |key| _id.match(/#{key}-\d+$/) }
      elsif keys.first.is_a?(String)
        keys.find { |key| _id.end_with?(key) }
      else # Regexp
        keys.find { |key| _id.match(key) }
      end
    end