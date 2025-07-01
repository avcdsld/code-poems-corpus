def places_to_param(places)
      places_to_param_config = { lat_lng_scale: configuration.lat_lng_scale }

      out = []
      polyline_encode_buffer = PolylineEncoderBuffer.new

      places.each do |place|
        if place.lat_lng? && configuration.use_encoded_polylines
          polyline_encode_buffer << place.lat_lng
        else
          polyline_encode_buffer.flush to: out
          out << escape(place.to_param(places_to_param_config))
        end
      end

      polyline_encode_buffer.flush to: out

      out.join(DELIMITER)
    end