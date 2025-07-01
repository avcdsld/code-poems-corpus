def to_bytes
      # Convert binary to hex, by slicing the binary in 4 bytes chuncks
      bitmap_hex = ""
      str = ""
      self.to_s.chars.reverse.each_with_index do |ch, i|
        str << ch
        next if i == 0
        if (i+1) % 4 == 0
          bitmap_hex << str.reverse.to_i(2).to_s(16)
          str = ""
        end
      end
      unless str.empty?
        bitmap_hex << str.reverse.to_i(2).to_s(16)
      end
      bitmap_hex.reverse.upcase
    end