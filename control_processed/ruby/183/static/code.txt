def touch(*names, time: nil)
      _raise_record_not_touched_error unless persisted?

      attribute_names = timestamp_attributes_for_update_in_model
      attribute_names |= names.map!(&:to_s).map! { |name|
        self.class.attribute_aliases[name] || name
      }

      unless attribute_names.empty?
        affected_rows = _touch_row(attribute_names, time)
        @_trigger_update_callback = affected_rows == 1
      else
        true
      end
    end