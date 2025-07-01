def check_curpos #:nodoc:
      # if the cursor is ahead of data in this row then move it back
      # i don't think this is required
      return
      if @pcol+@curpos > @buffer.length
        addcol((@pcol+@buffer.length-@curpos)+1)
        @curpos = @buffer.length 
        maxlen = (@maxlen || @width-@internal_width)

        # even this row is gt maxlen, i.e., scrolled right
        if @curpos > maxlen
          @pcol = @curpos - maxlen
          @curpos = maxlen-1 
        else
          # this row is within maxlen, make scroll 0
          @pcol=0
        end
        set_form_col 
      end
    end