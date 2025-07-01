def add(name, address)
      device = Device.new(name: name, address: address)
      self << device
      device
    end