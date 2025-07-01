def string_for l
    if RESERVED_LABELS.include? l
      l.to_s.capitalize
    else
      l.to_s
    end
  end