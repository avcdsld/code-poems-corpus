def get_config_files(name)
      files = []

      self.load_paths.reverse.each do |directory|
        # splatting *suffix allows us to deal with multipart suffixes
        name_no_overlay, suffixes = suffixes_for(name)
        suffixes.map { |suffix| [name_no_overlay, *suffix].compact.join('_') }.each do |name_with_suffix|
          self.file_types.each do |ext|
            filename = filename_for_name(name_with_suffix, directory, ext)
            if File.exists?(filename)
              modified_time = File.stat(filename).mtime
              files << [name, name_with_suffix, filename, ext, modified_time]
            end
          end
        end
      end

      logger.debug "get_config_files(#{name}) => #{files.select { |x| x[3] }.inspect}"

      files
    end