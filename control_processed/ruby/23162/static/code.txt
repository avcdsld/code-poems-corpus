def find_template_path(name, options = {})
      options = {
        prefer: "html", # Prefer a template with extension
      }.update(options)

      path = sanitize_name(name, options[:prefer])

      # Exact match
      return Pathname.new(path) if File.exist?(path)

      # Split extension and path
      path_extension, path_without_extension = split_path(path)

      # Get possible output extensions for path_extension
      template_extensions = template_extensions_for_output(path_extension, options[:prefer])

      # Let's look at the disk to see what files we've got
      files = Dir.glob(path_without_extension + ".*")

      results = filter_files(files, path, path_without_extension, template_extensions)

      if !results[0]
        # No results found, but maybe there is a directory
        # with the same name and it contains an index.XYZ
        find_template_path(File.join(name, "index")) if File.directory?(name)
      else
        Pathname.new(results[0])
      end
    end