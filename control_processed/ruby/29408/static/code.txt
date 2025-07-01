def lookup(setting, *args)
      setting = SettingPath.new setting if setting.is_a? String
      @provider.each do |provider|
        begin
          return special_value_or_string(provider.lookup(setting.clone, *args))
        rescue SettingNotFoundError; end
      end

      nil
    end