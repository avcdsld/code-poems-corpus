def add_recipient(recipient_type, address, variables = nil)
      # send the message when we have 1000, not before
      send_message if @counters[:recipients][recipient_type] == Mailgun::Chains::MAX_RECIPIENTS

      compiled_address = parse_address(address, variables)
      set_multi_complex(recipient_type, compiled_address)

      store_recipient_variables(recipient_type, address, variables) if recipient_type != :from

      @counters[:recipients][recipient_type] += 1 if @counters[:recipients].key?(recipient_type)
    end