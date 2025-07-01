def assign_to_or_mark_for_destruction(record, attributes, allow_destroy)
        record.assign_attributes(attributes.except(*UNASSIGNABLE_KEYS))
        record.mark_for_destruction if has_destroy_flag?(attributes) && allow_destroy
      end