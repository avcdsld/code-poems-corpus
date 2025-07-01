def guess_name(sections)
      if sections.size > 1
        sections[-1] = 'rails_db'
        variable     = sections.join("_")
        result       = eval(variable)
      end
    rescue NameError
      sections.delete_at(-2)
      guess_name(sections)
    end