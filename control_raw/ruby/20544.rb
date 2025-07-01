def custom_fields_basic_attributes
      {}.tap do |hash|
        self.non_relationship_custom_fields.each do |rule|
          name, type = rule['name'], rule['type'].to_sym

          # method of the custom getter
          method_name = "#{type}_attribute_get"

          hash.merge!(self.class.send(method_name, self, name))
        end
      end
    end