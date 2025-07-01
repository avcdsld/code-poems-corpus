def filter(tag, time, record)
      # Only generate and add an insertId field if the record is a hash and
      # the insert ID field is not already set (or set to an empty string).
      if record.is_a?(Hash) && record[@insert_id_key].to_s.empty?
        record[@insert_id_key] = increment_insert_id
      end
      record
    end