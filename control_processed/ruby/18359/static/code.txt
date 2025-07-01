def cursor=(coords)
      x, y = coords
      x = [x, 1].max
      y = [y, 0].max + 1
      @session.request(:nvim_eval, "cursor(#{x}, #{y})")
    end