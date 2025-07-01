def set_ext_attr(name, value)
      # this will raise an exception if the name doesn't exist
      ea_def = self.class::EXT_ATTRIB_CLASS.fetch name: name, api: api

      if ea_def.input_type == 'Pop-up Menu' && (!ea_def.popup_choices.include? value.to_s)
        raise JSS::UnsupportedError, "The value for #{name} must be one of: '#{ea_def.popup_choices.join("' '")}'"
      end

      unless value == JSS::BLANK
        case ea_def.data_type
        when 'Date'
          value = JSS.parse_datetime value

        when *NUMERIC_TYPES
          raise JSS::InvalidDataError, "The value for #{name} must be an integer" unless value.is_a? Integer

        end # case
      end # unless blank

      been_set = false
      @extension_attributes.each do |ea|
        next unless ea[:name] == name
        ea[:value] = value
        been_set = true
      end
      unless been_set
        @extension_attributes << { id: ea_def.id, name: name, type: ea_def.data_type, value: value }
      end

      @ext_attrs[name] = value
      @changed_eas << name
      @need_to_update = true
    end