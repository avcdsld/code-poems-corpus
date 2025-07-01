def contour_data
      x, y, z = coords
      return [x, y, z].transpose.flatten.join("\\")
    end