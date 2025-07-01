def adapt_example!(parsed_example)
      # Saving off the original data
      parsed_example['cuke_modeler_parsing_data'] = Marshal::load(Marshal.dump(parsed_example))

      # Removing parsed data for child elements in order to avoid duplicating data
      parsed_example['cuke_modeler_parsing_data'][:tags] = nil
      parsed_example['cuke_modeler_parsing_data'][:tableHeader] = nil
      parsed_example['cuke_modeler_parsing_data'][:tableBody] = nil

      parsed_example['keyword'] = parsed_example.delete(:keyword)
      parsed_example['name'] = parsed_example.delete(:name)
      parsed_example['line'] = parsed_example.delete(:location)[:line]
      parsed_example['description'] = parsed_example.delete(:description) || ''

      parsed_example['rows'] = []

      if parsed_example[:tableHeader]
        adapt_table_row!(parsed_example[:tableHeader])
        parsed_example['rows'] << parsed_example.delete(:tableHeader)
      end

      if parsed_example[:tableBody]

        parsed_example[:tableBody].each do |row|
          adapt_table_row!(row)
        end
        parsed_example['rows'].concat(parsed_example.delete(:tableBody))
      end


      parsed_example['tags'] = []
      parsed_example[:tags].each do |tag|
        adapt_tag!(tag)
      end
      parsed_example['tags'].concat(parsed_example.delete(:tags))
    end