def inputs
      self.class.filters.keys.each_with_object({}) do |name, h|
        h[name] = public_send(name)
      end
    end