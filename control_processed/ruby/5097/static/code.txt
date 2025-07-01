def extras_for_display
      merged_extras = []
      get_features.keys.each do |extra|
        # extras_field_key = "fieldLabels.extras.#{extra}"
        translated_option_key = I18n.t extra
        merged_extras.push translated_option_key

        # below check to ensure the field has not been deleted as
        # an available extra
        # quite an edge case - not entirely sure its worthwhile
        # if extras_field_configs[extras_field_key]
        #   translated_option_key = I18n.t extras_field_key
        #   merged_extras.push translated_option_key
        # end
      end
      merged_extras.sort{ |w1, w2| w1.casecmp(w2) }
      # above ensures sort is case insensitive
      # by default sort will add lowercased items to end of array
      # http://stackoverflow.com/questions/17799871/how-do-i-alphabetize-an-array-ignoring-case
      # return merged_extras.sort
    end