def store_autofilters   #:nodoc:
    # Skip all columns if no filter have been set.
    return '' if @filter_on == 0

    col1 = @filter_area.col_min
    col2 = @filter_area.col_max

    col1.upto(col2) do |i|
      # Reverse order since records are being pre-pended.
      col = col2 -i

      # Skip if column doesn't have an active filter.
      next unless @filter_cols[col]

      # Retrieve the filter tokens and write the autofilter records.
      store_autofilter(col, *@filter_cols[col])
    end
  end