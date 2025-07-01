def switch(*names)
      options = extract_options(names)
      names = [names].flatten

      verify_unused(names)
      switch = Switch.new(names,options)
      switches[switch.name] = switch

      clear_nexts
      switches_declaration_order << switch
      switch
    end