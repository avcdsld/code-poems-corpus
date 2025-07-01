def x=(val)
      left = x + center_x
      top = y + center_y

      if val < 0
        val = 0
      elsif val + image.width >= Window.width
        val = Window.width - image.width
      end

      super(val)

      draw_pen(left, top, x + center_x, y + center_y) if @enable_pen
    end