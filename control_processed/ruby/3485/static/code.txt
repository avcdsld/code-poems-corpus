def generate_any_value?(lm, hm)
      (lm.nil? || lm.is_a?(HQMF::AnyValue)) && (hm.nil? || hm.is_a?(HQMF::AnyValue))
    end