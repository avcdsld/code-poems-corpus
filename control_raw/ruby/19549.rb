def xf_record_index(row, col, xf=nil)       #:nodoc:
    if xf.respond_to?(:xf_index)
      xf.xf_index
    elsif @row_formats.has_key?(row)
      @row_formats[row].xf_index
    elsif @col_formats.has_key?(col)
      @col_formats[col].xf_index
    else
      0x0F
    end
  end