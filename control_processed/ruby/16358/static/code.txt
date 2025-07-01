def app_folders
      # Find all app folders
      @app_folders ||= begin
        volt_app    = File.expand_path(File.join(File.dirname(__FILE__), '../../../../app'))
        app_folders = [volt_app, "#{@root}/app", "#{@root}/vendor/app"].map { |f| File.expand_path(f) }

        # Gem folders with volt in them
        # TODO: we should probably qualify this a bit more
        app_folders += Gem.loaded_specs.values
                       .select {|gem| gem.name =~ /^volt/ }
                       .map {|gem| "#{gem.full_gem_path}/app" }

        app_folders.uniq
      end

      # Yield each app folder and return a flattened array with
      # the results

      files        = []
      @app_folders.each do |app_folder|
        files << yield(app_folder)
      end

      files.flatten
    end