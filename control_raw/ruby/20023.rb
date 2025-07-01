def merge_range_type(type, *args)
      case type
      when 'array_formula', 'blank', 'rich_string'
        row_first, col_first, row_last, col_last, *others = row_col_notation(args)
        format = others.pop
      else
        row_first, col_first, row_last, col_last, token, format, *others = row_col_notation(args)
      end

      raise "Format object missing or in an incorrect position" unless format.respond_to?(:xf_index)
      raise "Can't merge single cell" if row_first == row_last && col_first == col_last

      # Swap last row/col with first row/col as necessary
      row_first, row_last = row_last, row_first if row_first > row_last
      col_first, col_last = col_last, col_first if col_first > col_last

      # Check that column number is valid and store the max value
      check_dimensions(row_last, col_last)
      store_row_col_max_min_values(row_last, col_last)

      # Store the merge range.
      @merge << [row_first, col_first, row_last, col_last]

      # Write the first cell
      case type
      when 'blank', 'rich_string', 'array_formula'
        others << format
      end

      case type
      when 'string'
        write_string(row_first, col_first, token, format, *others)
      when 'number'
        write_number(row_first, col_first, token, format, *others)
      when 'blank'
        write_blank(row_first, col_first, *others)
      when 'date_time'
        write_date_time(row_first, col_first, token, format, *others)
      when 'rich_string'
        write_rich_string(row_first, col_first, *others)
      when 'url'
        write_url(row_first, col_first, token, format, *others)
      when 'formula'
        write_formula(row_first, col_first, token, format, *others)
      when 'array_formula'
        write_formula_array(row_first, col_first, *others)
      else
        raise "Unknown type '#{type}'"
      end

      # Pad out the rest of the area with formatted blank cells.
      write_formatted_blank_to_area(row_first, row_last, col_first, col_last, format)
    end