def post_process(intermediate_file, reduction_factor)
      # Calculate a new set of transforms with respect to reduction_factor
      transformation = if reduction_factor
                         reduce(without_crop, reduction_factor)
                       else
                         without_crop
                       end
      Riiif::File.new(intermediate_file).extract(transformation, image_info)
    end