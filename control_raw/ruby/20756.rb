def power_pins(id = nil, options = {}, &block)
      id, options = nil, id if id.is_a?(Hash)
      options = {
        power_pin: true
      }.merge(options)
      pins(id, options, &block)
    end