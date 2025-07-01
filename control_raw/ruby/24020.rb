def valid?
      REQUIRED_FIELDS[type].all? do |f|
        f.is_a?(Array) ? !(f & fields.keys).empty? : !fields[f].nil?
      end
    end