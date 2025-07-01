def recast opts={}
      opts.each do |vector_name, dtype|
        self[vector_name].cast(dtype: dtype)
      end
    end