def postprocess
      @position = @position.to_s.rjust(2, '0') if @position.to_s.size == 1
      @size &&= @size.to_i
      @raw = true if @raw == "true" unless @raw.is_a?(TrueClass)
      @mounted = (@mounted == "true") unless @mounted.is_a?(TrueClass)
    end