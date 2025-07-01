def paint  #:nodoc:
      my_win = nil
      if @form
        my_win = @form.window
      else
        my_win = @target_window
      end
      @graphic = my_win unless @graphic
      tm = get_content
      rc = tm.length
      _estimate_column_widths if rc > 0  # will set preferred_width 2011-10-4 
      @left_margin ||= @row_selected_symbol.length
      @width ||= @preferred_width

      @height ||= [tm.length+3, 10].min
      _prepare_format

      print_borders if (@suppress_borders == false && @repaint_all) # do this once only, unless everything changes
      _maxlen = @maxlen || @width-@internal_width
      tr = @toprow
      acolor = get_color $datacolor
      h = scrollatrow() 
      r,c = rowcol
      print_header
      r += @_header_adjustment # for column header
      @longest_line = @width #maxlen
      $log.debug " #{@name} Tabularwidget repaint width is #{@width}, height is #{@height} , maxlen #{maxlen}/ #{@maxlen}, #{@graphic.name} roff #{@row_offset} coff #{@col_offset}, r #{r} top #{toprow} ci #{current_index} "
      0.upto(h - @_header_adjustment) do |hh|
        crow = tr+hh
        if crow < rc
          #focussed = @current_index == crow ? true : false 
          content = tm[crow]

          columnrow = false
          if content == :columns
            columnrow = true
          end

          value = convert_value_to_text content, crow

          @buffer = value if crow == @current_index
          # next call modified string. you may wanna dup the string.
          # rlistbox does
          sanitize value if @sanitization_required
          truncate value
          ## set the selector symbol if requested
          paint_selector crow, r+hh, c, acolor, @attr

          #@graphic.printstring  r+hh, c, "%-*s" % [@width-@internal_width,value], acolor, @attr
          #print_data_row( r+hh, c, "%-*s" % [@width-@internal_width,value], acolor, @attr)
          print_data_row( r+hh, c+@left_margin, @width-@internal_width-@left_margin, value, acolor, @attr)

        else
          # clear rows
          @graphic.printstring r+hh, c, " " * (@width-@internal_width-@left_margin), acolor,@attr
        end
      end
      @repaint_required        = false
      @repaint_footer_required = true
      @repaint_all             = false

    end