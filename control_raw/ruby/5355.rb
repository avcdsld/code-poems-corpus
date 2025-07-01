def register_font(font_name, font_metrics, font_pdf_object, font_cmap = nil)
      new_font = Font.new
      new_font.name = font_name
      new_font.metrics = font_metrics
      new_font.cmap = font_cmap
      new_font[:is_reference_only] = true
      new_font[:referenced_object] = font_pdf_object
      FONTS_LIBRARY_MUTEX.synchronize do
        FONTS_LIBRARY[new_font.name] = new_font
      end
      new_font
    end