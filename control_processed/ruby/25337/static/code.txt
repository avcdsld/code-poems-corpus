def set_data_elements(options)
      @data_elements = []
      options.keys.sort.each do |tag|
        @data_elements << [ tag, options[tag] ] unless options[tag].nil?
      end
    end