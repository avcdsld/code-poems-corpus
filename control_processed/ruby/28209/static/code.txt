def next_column
      c = @column_pointer.next
      cp = @coffsets[c] 
      #$log.debug " next_column #{c} , #{cp} "
      @curpos = cp if cp
      next_row() if c < @column_pointer.last_index
      #addcol cp
      set_form_col 
    end