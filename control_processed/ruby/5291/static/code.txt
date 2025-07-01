def port=(new_port)
      if new_port != nil && new_port.respond_to?(:to_str)
        new_port = Addressable::URI.unencode_component(new_port.to_str)
      end

      if new_port.respond_to?(:valid_encoding?) && !new_port.valid_encoding?
        raise InvalidURIError, "Invalid encoding in port"
      end

      if new_port != nil && !(new_port.to_s =~ /^\d+$/)
        raise InvalidURIError,
          "Invalid port number: #{new_port.inspect}"
      end

      @port = new_port.to_s.to_i
      @port = nil if @port == 0

      # Reset dependent values
      remove_instance_variable(:@authority) if defined?(@authority)
      remove_instance_variable(:@normalized_port) if defined?(@normalized_port)
      remove_composite_values

      # Ensure we haven't created an invalid URI
      validate()
    end