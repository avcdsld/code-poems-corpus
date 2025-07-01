def load_pixel_data(dcm)
      raise ArgumentError, "Invalid argument 'dcm'. Expected DObject, got #{dcm.class}." unless dcm.is_a?(DICOM::DObject)
      raise ArgumentError, "Invalid argument 'dcm'. Expected modality 'CR', got #{dcm.value(MODALITY)}." unless dcm.value(MODALITY) == 'CR'
      # Set attributes common for all image modalities, i.e. CT, MR, RTDOSE & RTIMAGE:
      @dcm = dcm
      @narray = dcm.narray
      @date = dcm.value(IMAGE_DATE)
      @time = dcm.value(IMAGE_TIME)
      @columns = dcm.value(COLUMNS)
      @rows = dcm.value(ROWS)
      spacing = dcm.value(SPACING).split("\\")
      raise "Invalid DICOM image: 2 basckslash-separated values expected for Pixel Spacing, got: #{spacing}" unless spacing.length == 2
      @col_spacing = spacing[1].to_f
      @row_spacing = spacing[0].to_f
    end