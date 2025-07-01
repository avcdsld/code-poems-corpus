def find_default_key(key_names)
      key_names.each do |filename|
        path = Pathname.new(filename)
        # If we have a config location (like ./.chef/), look there first.
        if config_location
          local_path = path.expand_path(File.dirname(config_location))
          return local_path.to_s if local_path.exist?
        end
        # Then check ~/.chef.
        home_path = path.expand_path(home_chef_dir)
        return home_path.to_s if home_path.exist?
      end
      nil
    end