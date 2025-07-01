def handle_key ch #:nodoc:
      $log.debug " textview got ch #{ch} "
      @old_pcol = @pcol
      @buffer = @list[@current_index]
      if @buffer.nil? && row_count == 0
        @list << "\r"
        @buffer = @list[@current_index]
      end
      return if @buffer.nil?
      #$log.debug " before: curpos #{@curpos} blen: #{row_length}"
      if @curpos > row_length #@buffer.length
        addcol((row_length-@curpos)+1)
        @curpos = row_length
        set_form_col 
      end
      # We can improve later
      case ch
      when KEY_UP, ?k.getbyte(0)
        #select_prev_row
        ret = up
        # next removed as very irritating, can be configured if required 2011-11-2 
        #get_window.ungetch(KEY_BTAB) if ret == :NO_PREVIOUS_ROW
        check_curpos
        
      when KEY_DOWN, ?j.getbyte(0)
        ret = down
        # This should be configurable, or only if all rows are visible
        #get_window.ungetch(KEY_TAB) if ret == :NO_NEXT_ROW
        check_curpos
      #when KEY_LEFT, ?h.getbyte(0)
        #cursor_backward
      #when KEY_RIGHT, ?l.getbyte(0)
        #cursor_forward
      when ?\C-a.getbyte(0) #, ?0.getbyte(0)
        # take care of data that exceeds maxlen by scrolling and placing cursor at start
        @repaint_required = true if @pcol > 0 # tried other things but did not work
        set_form_col 0
        @pcol = 0
      when ?\C-e.getbyte(0), ?$.getbyte(0)
        # take care of data that exceeds maxlen by scrolling and placing cursor at end
        # This use to actually pan the screen to actual end of line, but now somewhere
        # it only goes to end of visible screen, set_form probably does a sanity check
        blen = row_length # @buffer.rstrip.length FIXME
        set_form_col blen
      when KEY_ENTER, FFI::NCurses::KEY_ENTER
        #fire_handler :PRESS, self
        fire_action_event
      when ?0.getbyte(0)..?9.getbyte(0)
        # FIXME the assumption here was that if numbers are being entered then a 0 is a number
        # not a beg-of-line command.
        # However, after introducing universal_argument, we can enters numbers using C-u and then press another
        # C-u to stop. In that case a 0 should act as a command, even though multiplier has been set
        if ch == ?0.getbyte(0) and $multiplier == 0
          # copy of C-a - start of line
          @repaint_required = true if @pcol > 0 # tried other things but did not work
          set_form_col 0
          @pcol = 0
          return 0
        end
        # storing digits entered so we can multiply motion actions
        $multiplier *= 10 ; $multiplier += (ch-48)
        return 0
      when ?\C-c.getbyte(0)
        $multiplier = 0
        return 0
      else
        # check for bindings, these cannot override above keys since placed at end
        begin
          ret = process_key ch, self
        rescue => err
          $log.error " TEXTVIEW ERROR #{err} "
          $log.debug(err.backtrace.join("\n"))
          textdialog [err.to_s, *err.backtrace], :title => "Exception"
        end
        return :UNHANDLED if ret == :UNHANDLED
      end
      $multiplier = 0 # you must reset if you've handled a key. if unhandled, don't reset since parent could use
      set_form_row
      return 0 # added 2010-01-12 22:17 else down arrow was going into next field
    end