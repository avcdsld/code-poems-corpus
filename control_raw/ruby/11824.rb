def inject_primary_key!(converted_props)
      self.class.default_property_values(self).tap do |destination_props|
        destination_props.merge!(converted_props) if converted_props.is_a?(Hash)
      end
    end