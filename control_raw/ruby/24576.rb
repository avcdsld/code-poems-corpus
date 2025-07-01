def save
      return true if !new_record? && !changed?
      raise Exceptions::ValidationFailedException.new(errors) if !valid?
      destroy(false) if !new_record?

      parent.modify_engine do |nat|
        nat.add_redirect(name, protocol, "", hostport, "", guestport)
      end

      clear_dirty!
      existing_record!
      true
    end