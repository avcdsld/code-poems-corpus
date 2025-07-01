def matte_floodfill(x, y)
      f = copy
      f.opacity = OpaqueOpacity unless f.alpha?
      target = f.pixel_color(x, y)
      f.matte_flood_fill(target, TransparentOpacity,
                         x, y, FloodfillMethod)
    end