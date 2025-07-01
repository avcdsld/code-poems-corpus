def search_upper_header(hdr)
      hdr.class.known_headers.each do |nh, bindings|
        return nh if bindings.check?(hdr)
      end

      nil
    end