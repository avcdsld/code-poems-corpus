def substitute_cellref(cell, *args)       #:nodoc:
    return [cell, *args] if cell.respond_to?(:coerce) # Numeric

    cell.upcase!

    # Convert a column range: 'A:A' or 'B:G'.
    # A range such as A:A is equivalent to A1:65536, so add rows as required
    if cell =~ /\$?([A-I]?[A-Z]):\$?([A-I]?[A-Z])/
      row1, col1 =  cell_to_rowcol($1 +'1')
      row2, col2 =  cell_to_rowcol($2 +'65536')
      return [row1, col1, row2, col2, *args]
    end

    # Convert a cell range: 'A1:B7'
    if cell =~ /\$?([A-I]?[A-Z]\$?\d+):\$?([A-I]?[A-Z]\$?\d+)/
      row1, col1 =  cell_to_rowcol($1)
      row2, col2 =  cell_to_rowcol($2)
      return [row1, col1, row2, col2, *args]
    end

    # Convert a cell reference: 'A1' or 'AD2000'
    if (cell =~ /\$?([A-I]?[A-Z]\$?\d+)/)
      row1, col1 =  cell_to_rowcol($1)
      return [row1, col1, *args]

    end

    raise("Unknown cell reference #{cell}")
  end