def error_in_changed_attributes?
      errs = errors

      changed_attributes.each_pair do |key, _|
        # If any of the fields with errors are also the ones that were
        return true if errs[key]
      end

      false
    end