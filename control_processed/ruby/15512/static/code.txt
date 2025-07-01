def add_directory(dir_path)
      full_path = File.join(@path, dir_path)
      FileUtils.mkdir_p(full_path) unless File.directory?(full_path)

      self.class.new(full_path)
    end