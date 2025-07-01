def select_next_field
      return :UNHANDLED if @widgets.nil? || @widgets.empty?
      #$log.debug "insdie sele nxt field :  #{@active_index} WL:#{@widgets.length}" 
      if @active_index.nil?  || @active_index == -1 # needs to be tested out A LOT
        # what is this silly hack for still here 2014-04-24 - 13:04  DELETE FIXME
        @active_index = -1 
      else
        f = @widgets[@active_index]
        begin
          on_leave f
        rescue FieldValidationException => err # added 2011-10-2 v1.3.1 so we can rollback
          $log.error "select_next_field: caught EXCEPTION #{err}"
          $error_message.value = "#{err}"
          raise err
        rescue => err
         $log.error "select_next_field: caught EXCEPTION #{err}"
         $log.error(err.backtrace.join("\n")) 
#         $error_message = "#{err}" # changed 2010  
         $error_message.value = "#{err}"
         Ncurses.beep
         return 0
        end
      end
      f = @widgets[@active_index]
      index = @focusables.index(f)
      # 2014-08-09 - 13:09 f may be status_line esp if ai is -1, so it is not found in focusables
      # why are we first checking widgets and then focusables.
      #index += 1
      index = index ? index+1 : 0
      f = @focusables[index]
      if f
        select_field f 
        return 0
      end
      #
      #$log.debug "insdie sele nxt field FAILED:  #{@active_index} WL:#{@widgets.length}" 
      ## added on 2008-12-14 18:27 so we can skip to another form/tab
      if @navigation_policy == :CYCLICAL
        f = @focusables.first
        if f
          select_field f
          return 0
        end
      end
      $log.debug "inside sele nxt field : NO NEXT  #{@active_index} WL:#{@widgets.length}" 
      return :NO_NEXT_FIELD
    end