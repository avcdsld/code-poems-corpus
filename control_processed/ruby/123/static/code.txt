def import(error, override_options = {})
      [:attribute, :type].each do |key|
        if override_options.key?(key)
          override_options[key] = override_options[key].to_sym
        end
      end
      @errors.append(NestedError.new(@base, error, override_options))
    end