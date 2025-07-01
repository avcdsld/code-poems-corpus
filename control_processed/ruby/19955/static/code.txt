def get_font_style_attributes(font)
      return [] unless font

      attributes = []
      attributes << ['sz', font[:_size]]      if ptrue?(font[:_size])
      attributes << ['b',  font[:_bold]]      if font[:_bold]
      attributes << ['i',  font[:_italic]]    if font[:_italic]
      attributes << ['u',  'sng']             if font[:_underline]

      # Turn off baseline when testing fonts that don't have it.
      if font[:_baseline] != -1
        attributes << ['baseline', font[:_baseline]]
      end
      attributes
    end