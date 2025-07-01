def bit(index, name, attrs = {})
      if index.is_a?(Range)
        msb = index.first
        lsb = index.last
        msb, lsb = lsb, msb if lsb > msb
        pos = lsb
        bits = (msb - lsb).abs + 1
      elsif index.is_a?(Numeric)
        pos = index
        bits = 1
      else
        fail 'No valid index supplied when defining a register bit!'
      end

      # Traynor, this could be more elegant
      # its just a dirty way to make the value of the
      # key in @new_reg_atts hash array (ie name) tie to
      # a value that is an array of hashes describing
      # data for each scrambled bit
      attrs = attrs.merge(pos: pos, bits: bits)
      temparray = []
      if @new_reg_attrs[name].nil?
        @new_reg_attrs[name] = attrs
      else
        if @new_reg_attrs[name].is_a? Hash
          temparray = temparray.push(@new_reg_attrs[name])
        else
          temparray = @new_reg_attrs[name]
        end
        temparray = temparray.push(attrs)
        # added the sort so that the order the registers bits is described is not important
        @new_reg_attrs[name] = temparray.sort { |a, b| b[:pos] <=> a[:pos] }

      end
    end