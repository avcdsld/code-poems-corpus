def write_legend # :nodoc:
      position = @legend_position.sub(/^overlay_/, '')
      return if position == 'none' || (not position_allowed.has_key?(position))

      @delete_series = @legend_delete_series if @legend_delete_series.kind_of?(Array)
      @writer.tag_elements('c:legend') do
        # Write the c:legendPos element.
        write_legend_pos(position_allowed[position])
        # Remove series labels from the legend.
        # Write the c:legendEntry element.
        @delete_series.each { |i| write_legend_entry(i) } if @delete_series
        # Write the c:layout element.
        write_layout(@legend_layout, 'legend')
        # Write the c:txPr element.
        write_tx_pr(nil, @legend_font) if ptrue?(@legend_font)
        # Write the c:overlay element.
        write_overlay if @legend_position =~ /^overlay_/
      end
    end