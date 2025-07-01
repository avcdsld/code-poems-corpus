def guess_first_header(binary_str)
      first_header = nil
      Header.all.each do |hklass|
        hdr = hklass.new(packet: self)
        # #read may return another object (more specific class)
        hdr = hdr.read(binary_str)
        # First header is found when, for one known header,
        # * +#parse?+ is true
        # * it exists a known binding with a upper header
        next unless hdr.parse?

        first_header = hklass.to_s.gsub(/.*::/, '') if search_upper_header(hdr)
        break unless first_header.nil?
      end
      first_header
    end