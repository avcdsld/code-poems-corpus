def formatted_switches
      [
        switches.first.rjust(10),
        switches.last.ljust(13),
      ].join(", ").gsub(%r! , !, "   ").gsub(%r!,   !, "    ")
    end