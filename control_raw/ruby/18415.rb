def assert_xy!(x, y)
      unless include_xy?(x, y)
        raise ChunkyPNG::OutOfBounds, "Coordinates (#{x},#{y}) out of bounds!"
      end
      true
    end