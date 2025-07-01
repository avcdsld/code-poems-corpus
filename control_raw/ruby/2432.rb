def undo
      case action
      when 'create'
        # destroys a newly created record
        auditable.destroy!
      when 'destroy'
        # creates a new record with the destroyed record attributes
        auditable_type.constantize.create!(audited_changes)
      when 'update'
        # changes back attributes
        auditable.update_attributes!(audited_changes.transform_values(&:first))
      else
        raise StandardError, "invalid action given #{action}"
      end
    end