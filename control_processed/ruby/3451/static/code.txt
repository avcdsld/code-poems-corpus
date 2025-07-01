def px_to_window_rel(opts = {}, driver = $driver)
      w = driver.window_size
      x = opts.fetch :x, 0
      y = opts.fetch :y, 0

      OpenStruct.new(x: "#{x.to_f} / #{w.width.to_f}",
                     y: "#{y.to_f} / #{w.height.to_f}")
    end