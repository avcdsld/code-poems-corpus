def angle=(val)
      val %= 360
      radian = val * Math::PI / 180
      @vector[:x] = Math.cos(radian)
      @vector[:y] = Math.sin(radian)

      if @rotation_style == :free
        self.scale_x = scale_x.abs
        super(val)
      elsif @rotation_style == :left_right
        if @vector[:x] >= 0
          self.scale_x = scale_x.abs
        else
          self.scale_x = scale_x.abs * -1
        end
        super(0)
      else
        self.scale_x = scale_x.abs
        super(0)
      end
    end