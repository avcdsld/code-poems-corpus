def handle_attribute_code(attribute, code, name)
      null_flavor = attribute.at_xpath('./cda:code/@nullFlavor', NAMESPACES).try(:value)
      o_text = attribute.at_xpath('./cda:code/cda:originalText/@value', NAMESPACES).try(:value)
      code_obj = HQMF::Coded.new(attribute.at_xpath('./cda:code/@xsi:type', NAMESPACES).try(:value) || 'CD',
                                 attribute.at_xpath('./cda:code/@codeSystem', NAMESPACES).try(:value),
                                 code,
                                 attribute.at_xpath('./cda:code/@valueSet', NAMESPACES).try(:value),
                                 name,
                                 null_flavor,
                                 o_text)
      [code_obj, null_flavor, o_text]
    end