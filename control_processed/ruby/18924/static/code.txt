def parents(obj)
      result = []
      cursor = obj
      while (cursor = cursor.parent)
        result << cursor
      end
      result
    end