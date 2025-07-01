def build_attribute_values(attributes, parsed_hashes)
      [].tap do |attribute_values|
        attributes.each do |key, static_value|
          attribute_values << AttributeValue.new(:static, key, static_value)
        end
        parsed_hashes.each do |parsed_hash|
          parsed_hash.each do |key, dynamic_value|
            attribute_values << AttributeValue.new(:dynamic, key, dynamic_value)
          end
        end
      end
    end