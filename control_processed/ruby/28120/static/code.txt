def insert_line lineno=@current_index
      prompt = "Insert: "
      maxlen = 80
      #config={}; 
      #config[:default] = line
      #ret, str = rb_getstr(@form.window, $error_message_row, $error_message_col,  prompt, maxlen, config)
      ret, str = input_string prompt
      #ret, str = rb_getstr(@form.window, @row+@height-1, @col+1, prompt, maxlen, config)
      $log.debug " rb_getstr returned #{ret} , #{str} "
      return if ret != 0

      # pad based expect @content not list
      # remove list after a while FIXME
      @list ||= @content
      @list.insert lineno, str
      ## added handler on 2010-05-23 11:46 - undo works - tested in testlistbox.rb
      fire_handler :CHANGE, InputDataEvent.new(0,str.length, self, :INSERT_LINE, lineno, str)
      fire_dimension_changed
    end