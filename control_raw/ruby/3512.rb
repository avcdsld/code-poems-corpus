def handle_mapping_template(mapping)
      if mapping
        if mapping[:valueset_path] && @entry.at_xpath(mapping[:valueset_path])
          @code_list_xpath = mapping[:valueset_path]
        end
        @value = DataCriteriaMethods.parse_value(@entry, mapping[:result_path]) if mapping[:result_path]
      end
    end