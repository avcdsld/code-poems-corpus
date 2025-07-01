def record_unchanged?(record_new, record_old)
      # NOTE: Using the dirty state would be great here, but it doesn't keep track of
      # in-place changes.

      allow_indexing?(record_old) == allow_indexing?(record_new) &&
        !@fields.map { |field| record_old.send(field) == record_new.send(field) }.include?(false)
    end