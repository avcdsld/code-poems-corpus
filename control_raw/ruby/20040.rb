def position_object_emus(col_start, row_start, x1, y1, width, height, x_dpi = 96, y_dpi = 96) #:nodoc:
      col_start, row_start, x1, y1, col_end, row_end, x2, y2, x_abs, y_abs =
        position_object_pixels(col_start, row_start, x1, y1, width, height)

      # Convert the pixel values to EMUs. See above.
      x1    = (0.5 + 9_525 * x1).to_i
      y1    = (0.5 + 9_525 * y1).to_i
      x2    = (0.5 + 9_525 * x2).to_i
      y2    = (0.5 + 9_525 * y2).to_i
      x_abs = (0.5 + 9_525 * x_abs).to_i
      y_abs = (0.5 + 9_525 * y_abs).to_i

      [col_start, row_start, x1, y1, col_end, row_end, x2, y2, x_abs, y_abs]
    end