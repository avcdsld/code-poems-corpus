def build(*args)
      raise StandardError, "Cannot build property without a class" if @type.nil?

      if @init_method.is_a?(Proc)
        @init_method.call(*args)
      else
        @type.send(@init_method, *args)
      end
    end