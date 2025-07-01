def limit_records(records)
      offset = self.offset
      limit  = self.limit
      size   = records.size

      if offset > size - 1
        []
      elsif (limit && limit != size) || offset > 0
        records[offset, limit || size] || []
      else
        records.dup
      end
    end