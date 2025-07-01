def change_font_italics(italicized = false)
      validate_worksheet

      font = get_cell_font.dup
      font.set_italic(italicized)
      update_font_references(font)
    end