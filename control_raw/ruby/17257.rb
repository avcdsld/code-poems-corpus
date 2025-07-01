def pause(remaining_pause_cycles)
      builder = XML.new("<subscription/>")
      builder.add_element('remaining_pause_cycles', remaining_pause_cycles)
      reload API.put("#{uri}/pause", builder.to_s)
      true
    end