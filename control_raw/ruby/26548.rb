def create_drr(series=nil, options={})
      raise ArgumentError, "Invalid argument 'series'." if series && !series.is_a?(RTImage)
      raise "This Beam instance has no associated control points. Unable to provide enough information to create a DRR." unless @control_points.length > 0
      # Get the necessary information from the first associated control point:
      gantry_angle = @control_points.first.gantry_angle
      isocenter = @control_points.first.iso
      # Set default values to undefined options:
      columns = options[:columns] || 512
      rows = options[:rows] || 512
      delta_col = options[:delta_col] || 1.0
      delta_row = options[:delta_row] || 1.0
      sdd = options[:sdd] || 1600.0
      sid = options[:sid] || 1000.0
      # Create an RT Image series if not given:
      series = RTImage.new(RTKIT.series_uid, @plan) unless series
      # Create a voxel space from the associated image series:
      vs = @plan.struct.image_series.first.to_voxel_space
      # Create a DRR pixel space:
      ps = PixelSpace.setup(columns, rows, delta_col, delta_row, gantry_angle, sdd, isocenter)
      # Create a beam geometric setup:
      bg = BeamGeometry.setup(gantry_angle, sid, isocenter, vs)
      # Create the DRR image data:
      bg.create_drr(ps)
      # Create the DRR DICOM projection image instance:
      drr = ProjectionImage.new(RTKIT.sop_uid, series, :beam => self)
      drr.columns = columns
      drr.rows = rows
      drr.row_spacing = ps.delta_row
      drr.col_spacing = ps.delta_col
      # Transfer data from the pixel space to the projection image:
      drr.narray = NArray.new(NArray::SINT, columns, rows)
      drr.narray[] = ps
      drr.set_positions
      # Return the DRR (DICOM image) instance:
      drr
    end