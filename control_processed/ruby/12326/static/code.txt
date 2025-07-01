def format_types(list, brackets = true)
      list.nil? || list.empty? ? "" : (brackets ? "(#{list.join(", ")})" : list.join(", "))
    end