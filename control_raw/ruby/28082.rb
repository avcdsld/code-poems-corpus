def clear_selection
      return if @selected_indices.nil? || @selected_indices.empty?
      arr = @selected_indices.dup # to un highlight
      @selected_indices.clear
      arr.each {|i| @obj.fire_row_changed(i) }
      @selected_index = nil
      @old_selected_index = nil
      #  User should ignore first two params
      lse = ListSelectionEvent.new(0, arr.size, @obj, :CLEAR)
      @obj.fire_handler :LIST_SELECTION_EVENT, lse
      arr = nil
    end