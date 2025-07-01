def plugin_files_by_dir(plugin_dir = Ohai.config[:plugin_path])
      Array(plugin_dir).map do |path|
        if Dir.exist?(path)
          Ohai::Log.trace("Searching for Ohai plugins in #{path}")

          escaped = ChefConfig::PathHelper.escape_glob_dir(path)
          Dir[File.join(escaped, "**", "*.rb")]
        else
          Ohai::Log.debug("The plugin path #{path} does not exist. Skipping...")
          []
        end
      end.flatten
    end