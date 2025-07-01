def parse_crop_line(line)
      new_line = @crop_line_default.merge line
      new_line['width'] = Args::UnitConversion.parse(new_line['width'], @dpi)
      new_line['color'] = colorify new_line['color']
      new_line['style_desc'] = new_line['style']
      new_line['style'] = Sprues::CropLineDash.new(new_line['style'], @dpi)
      new_line['line'] = Sprues::CropLine.new(
        new_line['type'], new_line['position'], sheet_width, sheet_height, @dpi
      )
      new_line
    end