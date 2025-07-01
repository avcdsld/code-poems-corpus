def has_attribute(*args)

      args.each { |a| a = a.to_s; return a if attributes[a] != nil }

      nil
    end