def write_date_time(*args)
      # Check for a cell reference in A1 notation and substitute row and column
      row, col, str, xf = row_col_notation(args)
      raise WriteXLSXInsufficientArgumentError if [row, col, str].include?(nil)

      # Check that row and col are valid and store max and min values
      check_dimensions(row, col)
      store_row_col_max_min_values(row, col)

      date_time = convert_date_time(str)

      if date_time
        store_data_to_table(NumberCellData.new(self, row, col, date_time, xf))
      else
        # If the date isn't valid then write it as a string.
        write_string(*args)
      end
    end