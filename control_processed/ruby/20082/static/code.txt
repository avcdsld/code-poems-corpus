def write_a_xfrm(col_absolute, row_absolute, width, height, shape = nil)
      attributes = []

      rotation = shape ? shape.rotation : 0
      rotation *= 60000

      attributes << ['rot', rotation] if rotation != 0
      attributes << ['flipH', 1]      if shape && ptrue?(shape.flip_h)
      attributes << ['flipV', 1]      if shape && ptrue?(shape.flip_v)

      @writer.tag_elements('a:xfrm', attributes) do
        # Write the a:off element.
        write_a_off( col_absolute, row_absolute )
        # Write the a:ext element.
        write_a_ext( width, height )
      end
    end