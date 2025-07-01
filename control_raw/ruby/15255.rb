def code(*colors)
      attribute = []
      colors.each do |color|
        value = ANSI::ATTRIBUTES[color] || ALIASES[color]
        if value
          attribute << value
        else
          validate(color)
        end
      end
      attribute
    end