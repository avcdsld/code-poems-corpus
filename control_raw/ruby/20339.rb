def default_values
      h = {}
      template.parameters.each do |p|
        h[p.name] = h.default
      end
      h
    end