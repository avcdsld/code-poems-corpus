def add_pin(id = nil, options = {}, &_block)
      id, options = nil, id if id.is_a?(Hash)
      power_pin = options.delete(:power_pin)
      ground_pin = options.delete(:ground_pin)
      virtual_pin = options.delete(:virtual_pin)
      other_pin = options.delete(:other_pin)
      if options[:size] && options[:size] > 1
        group = PinCollection.new(self, options.merge(placeholder: true))
        group.id = id if id
        options = {
          name: ''
        }.merge(options)

        rtl_name = options[:rtl_name]
        force = options[:force]
        offset = options.delete(:offset) || 0
        options.delete(:size).times do |i|
          pin_index = offset + i
          options[:name] = "#{id}#{pin_index}".to_sym
          options[:rtl_name] = "#{rtl_name}#{pin_index}".to_sym if rtl_name
          options[:force] = force[pin_index] if force

          if power_pin
            group[i] = PowerPin.new(pin_index, self, options)
          elsif ground_pin
            group[i] = GroundPin.new(pin_index, self, options)
          elsif virtual_pin
            group[i] = VirtualPin.new(pin_index, self, options)
          elsif other_pin
            group[i] = OtherPin.new(pin_index, self, options)
          else
            group[i] = Pin.new(pin_index, self, options)
          end
          group[i].invalidate_group_cache
        end
        yield group if block_given?
        group.each do |pin|
          pin.send(:primary_group_index=, pin.id)
          pin.id = "#{group.id}#{pin.id}".to_sym
          pin.send(:primary_group=, group)
          pin.finalize
        end
        if group.size == 1
          Origen.pin_bank.add_pin(group.first, self, options)
        else
          Origen.pin_bank.add_pin_group(group, self, options)
        end
      else
        if power_pin
          pin = PowerPin.new(id || :temp, self, options)
        elsif ground_pin
          pin = GroundPin.new(id || :temp, self, options)
        elsif virtual_pin
          pin = VirtualPin.new(id || :temp, self, options)
        elsif other_pin
          pin = OtherPin.new(id || :temp, self, options)
        else
          pin = Pin.new(id || :temp, self, options)
        end
        yield pin if block_given?
        pin.finalize
        Origen.pin_bank.add_pin(pin, self, options)
      end
    end