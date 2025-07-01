def sum
      if @sum
        # If the sum volume has already been created, return it instead of recreating:
        return @sum
      else
        if @volumes.length > 0
          nr_frames = @volumes.first.images.length
          # Create the sum DoseVolume instance:
          sop_uid = @volumes.first.sop_uid + ".1"
          @sum = DoseVolume.new(sop_uid, @volumes.first.frame, @volumes.first.dose_series, :sum => true)
          # Sum the dose of the various DoseVolumes:
          dose_sum = NArray.int(nr_frames, @volumes.first.images.first.columns, @volumes.first.images.first.rows)
          @volumes.each { |volume| dose_sum += volume.dose_arr }
          # Convert dose float array to integer pixel values of a suitable range,
          # along with a corresponding scaling factor:
          sum_scaling_coeff = dose_sum.max / 65000.0
          if sum_scaling_coeff == 0.0
            pixel_values = NArray.int(nr_frames, @volumes.first.images.first.columns, @volumes.first.images.first.rows)
          else
            pixel_values = dose_sum * (1 / sum_scaling_coeff)
          end
          # Set the scaling coeffecient:
          @sum.scaling = sum_scaling_coeff
          # Collect the rest of the image information needed to create new dose images:
          sop_uids = RTKIT.sop_uids(nr_frames)
          slice_positions = @volumes.first.images.collect {|img| img.pos_slice}
          columns = @volumes.first.images.first.columns
          rows = @volumes.first.images.first.rows
          pos_x = @volumes.first.images.first.pos_x
          pos_y = @volumes.first.images.first.pos_y
          col_spacing = @volumes.first.images.first.col_spacing
          row_spacing = @volumes.first.images.first.row_spacing
          cosines = @volumes.first.images.first.cosines
          # Create dose images for our sum dose volume:
          nr_frames.times do |i|
            img = SliceImage.new(sop_uids[i], slice_positions[i], @sum)
            # Fill in image information:
            img.columns = columns
            img.rows = rows
            img.pos_x = pos_x
            img.pos_y = pos_y
            img.col_spacing = col_spacing
            img.row_spacing = row_spacing
            img.cosines = cosines
            # Fill in the pixel frame data:
            img.narray = pixel_values[i, true, true]
          end
          return @sum
        end
      end
    end