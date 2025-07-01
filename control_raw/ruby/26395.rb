def setup(contour_sequence)
      raise ArgumentError, "Invalid argument 'contour_sequence'. Expected DICOM::Sequence, got #{contour_sequence.class}." unless contour_sequence.is_a?(DICOM::Sequence)
      contour_item = contour_sequence[0]
      # Image reference:
      sop_uid = contour_item[CONTOUR_IMAGE_SQ][0].value(REF_SOP_UID)
      @image = @frame.image(sop_uid)
      # POI coordinates:
      self.coordinate = Coordinate.new(*contour_item.value(CONTOUR_DATA).split("\\")[0..2])
    end