def assign_all_attributes(attrs, track_changes = false)
      # Assign each attribute using setters
      attrs.each_pair do |key, value|
        key = key.to_sym

        # Track the change, since assign_all_attributes runs with no_change_tracking
        old_val = @attributes[key]
        attribute_will_change!(key, old_val) if track_changes && old_val != value

        if self.respond_to?(:"#{key}=")
          # If a method without an underscore is defined, call that.
          send(:"#{key}=", value)
        else
          # Otherwise, use the _ version
          set(key, value)
        end
      end

      # Make an id if there isn't one yet
      if @attributes[:id].nil? && persistor.try(:auto_generate_id)
        @attributes[:id] = generate_id
      end
    end