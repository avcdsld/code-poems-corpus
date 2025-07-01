def num_cells_in_range(str)
      cells = str.split(':')
      return 1 if cells.count == 1
      raise ArgumentError.new("invalid range string: #{str}. Supported range format 'A1:B2'") if cells.count != 2
      x1, y1 = extract_coordinate(cells[0])
      x2, y2 = extract_coordinate(cells[1])
      (x2 - (x1 - 1)) * (y2 - (y1 - 1))
    end