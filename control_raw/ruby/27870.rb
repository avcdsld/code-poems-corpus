def list *val
      return @list if val.empty?
      alist = val[0]
      case alist
      when Array
        @list = alist
        # I possibly should call init_vars in these 3 cases but am doing the minimal 2013-04-10 - 18:27 
        # Based no issue: https://github.com/mare-imbrium/canis/issues/15
        @current_index = @toprow = @pcol = 0
      when NilClass
          @list = [] # or nil ?
          @current_index = @toprow = @pcol = 0
      when Variable
        @list = alist.value
        @current_index = @toprow = @pcol = 0
      else
        raise ArgumentError, "Listbox list(): do not know how to handle #{alist.class} " 
      end
      clear_selection
    
      @repaint_required = true
      @widget_scrolled = true  # 2011-10-15 
      @list
    end