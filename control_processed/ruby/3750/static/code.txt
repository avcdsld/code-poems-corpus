def delete(v)
      return unless include? v
      raise ArgumentError, "Item is protected and cannot be deleted" if protected? index(v)
      @list.delete v
    end