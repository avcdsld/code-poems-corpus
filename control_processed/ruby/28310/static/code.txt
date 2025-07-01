def show_caret_func
      return unless @show_caret
      # trying highlighting cursor 2010-01-23 19:07 TABBEDPANE TRYING
      # TODO take into account rows_panned etc ? I don't think so.
      @rows_panned ||= 0
      r,c = rowcol
      yy = r + @current_index - @toprow - @win_top
      #xx = @form.col # how do we know what value has been set earlier ?
      yy = r + @current_index - @toprow #- @win_top
      yy = @row_offset + @current_index - @toprow #- @win_top
      xx = @col_offset + @curpos || 0
      #yy = @row_offset if yy < @row_offset # sometimes r is 0, we are missing something in tabbedpane+scroll
      #xx = @col_offset if xx < @col_offset
      #xx = 0 if xx < 0

      $log.debug " #{@name} printing CARET at #{yy},#{xx}: fwt:- #{@win_top} r:#{@row} tr:-#{@toprow}+ci:#{@current_index},+r #{r}  "
      if !@oldcursorrow.nil?
        @graphic.mvchgat(y=@oldcursorrow, x=@oldcursorcol, 1, Ncurses::A_NORMAL, $datacolor, NIL)
      end
      @oldcursorrow = yy
      @oldcursorcol = xx
      @graphic.mvchgat(y=yy, x=xx, 1, Ncurses::A_NORMAL, $reversecolor, nil)
      @buffer_modified = true
    end