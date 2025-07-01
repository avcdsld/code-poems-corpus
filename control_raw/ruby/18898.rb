def geo_to_h3(coords, resolution)
      raise ArgumentError unless coords.is_a?(Array) && coords.count == 2

      lat, lon = coords

      if lat > 90 || lat < -90 || lon > 180 || lon < -180
        raise(ArgumentError, "Invalid coordinates")
      end

      coords = GeoCoord.new
      coords[:lat] = degs_to_rads(lat)
      coords[:lon] = degs_to_rads(lon)
      Bindings::Private.geo_to_h3(coords, resolution)
    end