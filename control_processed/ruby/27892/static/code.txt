def OLDprint_borders
      window = @graphic # 2009-12-26 14:54 BUFFERED
      @color_pair = get_color($datacolor) # 2011-09-28 V1.3.1 
      bordercolor = @border_color || @color_pair
      borderatt = @border_attrib || Ncurses::A_NORMAL
      #color = $datacolor
      #window.print_border @row, @col, @height, @width, color
      window.print_border @row, @col, @height-1, @width, bordercolor, borderatt
      print_title
=begin
      hline = "+%s+" % [ "-"*(width-((1)*2)) ]
      hline2 = "|%s|" % [ " "*(width-((1)*2)) ]
      window.printstring( row=startrow, col=startcol, hline, color)
      print_title
      (startrow+1).upto(startrow+height-1) do |row|
        window.printstring(row, col=startcol, hline2, color)
      end
      window.printstring(startrow+height, col=startcol, hline, color)
=end
  
    end