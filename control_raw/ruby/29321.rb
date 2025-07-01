def tml_options_for_select(options, selected = nil, description = nil, lang = Tml.session.current_language)
      options_for_select(options.tro(description), selected)
    end