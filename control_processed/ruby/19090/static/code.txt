def assign_nested_attributes(association_name, attributes, options = {})
      attributes = validate_attributes(attributes)
      association_name = association_name.to_sym
      send("#{association_name}=", []) if send(association_name).nil?

      attributes.each_value do |params|
        if params['id'].blank?
          unless reject_new_record?(params, options)
            new = association_name.to_c.new(params.except(*UNASSIGNABLE_KEYS))
            send(association_name).push(new)
          end
        else
          existing = send(association_name).detect { |record| record.id.to_s == params['id'].to_s }
          assign_to_or_mark_for_destruction(existing, params)
        end
      end
      (self.nested_attributes ||= []).push(association_name)
    end