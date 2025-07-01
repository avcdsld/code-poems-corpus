def repaint
      return unless @repaint_required
      @height ||= 10
      @width  ||= 30
    
      my_win = @form ? @form.window : @target_window
      @graphic = my_win unless @graphic
   
      raise " #{@name} neither form, nor target window given TV paint " unless my_win
      raise " #{@name} NO GRAPHIC set as yet                 TV paint " unless @graphic
      #@win_left = my_win.left
      #@win_top = my_win.top

      $log.debug "rtree repaint  #{@name} graphic #{@graphic}"
      print_borders unless @suppress_borders # do this once only, unless everything changes
      maxlen = @maxlen || @width-@internal_width
      maxlen -= @left_margin # 2011-10-6 
      tm = _list()
      select_default_values
      rc = row_count
      tr = @toprow
      acolor = get_color $datacolor
      h = scrollatrow()
      r,c = rowcol
      @longest_line = @width #maxlen
      0.upto(h) do |hh|
        crow = tr+hh
        if crow < rc
            _focussed = @current_index == crow ? true : false  # row focussed ?
            focus_type = _focussed 
            # added 2010-09-02 14:39 so inactive fields don't show a bright focussed line
            #focussed = false if focussed && !@focussed
            focus_type = :SOFT_FOCUS if _focussed && !@focussed
            selected = row_selected? crow 
            content = tm[crow]   # 2009-01-17 18:37 chomp giving error in some cases says frozen
            if content.is_a? TreeNode
              node = content
              object = content
              leaf = node.is_leaf?
              # content passed is rejected by treecellrenderer 2011-10-6 
              content = node.user_object.to_s # may need to trim or truncate
              expanded = row_expanded? crow  
            elsif content.is_a? String
              $log.warn "Removed this entire block since i don't think it was used XXX  "
              # this block does not set object XXX
            else
              raise "repaint what is the class #{content.class} "
              content = content.to_s
            end
            # this is redundant since data is taken by renderer directly
            #sanitize content if @sanitization_required
            #truncate value
            ## set the selector symbol if requested
            selection_symbol = ''
            if @show_selector
              if selected
                selection_symbol = @row_selected_symbol
              else
                selection_symbol =  @row_unselected_symbol
              end
              @graphic.printstring r+hh, c, selection_symbol, acolor,@attr
            end

            renderer = cell_renderer()
            renderer.display_length(@width-@internal_width-@left_margin) # just in case resizing of listbox
            renderer.pcol = @pcol
            #renderer.repaint @graphic, r+hh, c+@left_margin, crow, content, _focussed, selected
            renderer.repaint @graphic, r+hh, c+@left_margin, crow, object, content, leaf,  focus_type, selected, expanded
            @longest_line = renderer.actual_length if renderer.actual_length > @longest_line 
        else
          # clear rows
          @graphic.printstring r+hh, c, " " * (@width-@internal_width), acolor,@attr
        end
      end
      @table_changed = false
      @repaint_required = false
    end