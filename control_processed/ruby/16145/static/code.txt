def add(sql, extras = nil)
      return self if sql.nil? || sql.empty?

      query << " " unless query.empty?
      query << interpolate(sql.strip, extras)

      self
    end