def loadAttributes(attribType)
      result = []

      # ad is an attribute descriptor.
      @list.each do |ad|
        next unless ad['attrib_type'] == attribType

        # Load referenced attribute and add it to parent.
        result += @boot_sector.mftEntry(ad['mft']).loadAttributes(attribType)
      end

      result
    end