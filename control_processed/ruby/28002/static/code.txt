def goto_last_item
      bc = @buttons.count
      f = nil
      @components[bc..-1].each { |c| 
        if c.focusable
          f = c
        end
      }
      if f
        leave_current_component
        @current_component = f
        set_form_row
      end
    end