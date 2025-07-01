def rectangle_zone(top_left_lat, top_left_lon,
                       bottom_right_lat, bottom_right_lon,
                       map_zoom, options = {})
      url = 'http://api.openweathermap.org/data/2.5/box/city'
      bbox = encode_array [top_left_lat, top_left_lon, bottom_right_lat,
              bottom_right_lon, map_zoom]
      new(options.merge(bbox: bbox)).retrieve url
    end