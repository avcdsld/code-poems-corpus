def prepare_formats #:nodoc:
      @formats.formats.each do |format|
        xf_index  = format.xf_index
        dxf_index = format.dxf_index

        @xf_formats[xf_index] = format   if xf_index
        @dxf_formats[dxf_index] = format if dxf_index
      end
    end