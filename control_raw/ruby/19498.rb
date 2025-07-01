def convert_ref2d(cell, _class)
    # Convert the cell reference
    row, col = cell_to_packed_rowcol(cell)

    # The ptg value depends on the class of the ptg.
    if    (_class == 0)
      ptgref = [@ptg['ptgRef']].pack("C")
    elsif (_class == 1)
      ptgref = [@ptg['ptgRefV']].pack("C")
    elsif (_class == 2)
      ptgref = [@ptg['ptgRefA']].pack("C")
    else
      exit "Unknown function class in formula\n"
    end

    ptgref + row + col
  end