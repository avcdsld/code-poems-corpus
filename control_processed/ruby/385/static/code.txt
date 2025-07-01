def require_plugin_files
      unless site.safe
        plugins_path.each do |plugin_search_path|
          plugin_files = Utils.safe_glob(plugin_search_path, File.join("**", "*.rb"))
          Jekyll::External.require_with_graceful_fail(plugin_files)
        end
      end
    end