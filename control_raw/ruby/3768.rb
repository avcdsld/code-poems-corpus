def serialized_attributes(str = '', additional_attributes = {})
      attributes = declared_attributes.merge! additional_attributes
      attributes.each do |key, value|
        str << "#{Axlsx.camel(key, false)}=\"#{Axlsx.camel(Axlsx.booleanize(value), false)}\" "
      end
      str
    end