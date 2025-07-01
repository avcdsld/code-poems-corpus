def next_match str, startline=nil, endline=nil
      # 1. look in current row after the curpos
      # 2. if no match look in rest of array
      # 3. if no match and you started from current_index, then search
      #   from start of file to current_index. call _next_match with 0.
      _arr = _getarray
      if !startline
        startline = @current_index
        pos = @curpos + 1
        # FIXME you could be at end of line
        #_line = _arr[startline]
        _line = to_searchable(startline)
        _col = _line.index(str, pos) if _line
        if _col
          return [startline, _col]
        end
        startline += 1 # FIXME check this end of file
      end
       # FIXME iterate only through the ones we need, not all
      _arr.each_with_index do |line, ix|
        next if ix < startline
        break if endline && ix > endline
        # next line just a hack and not correct if only one match in file FIXME
        line = to_searchable(ix)
        _col = line.index str
        if _col
          return [ix, _col]
        end
      end
      if startline > 0
        return next_match str, 0, @current_index
      end
      return nil

    end