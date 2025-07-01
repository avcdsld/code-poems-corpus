def extract_file_layout(path, ignore=[])
      return [] unless File.directory?(path)
      dirs = []
      files = []
      ignore += [ '.', '..' ]
      Dir.foreach(path) do |f|
        next if ignore.include?(f)
        full_path = File.join(path, f)
        if File.directory?(full_path)
          dirs << { f => extract_file_layout(full_path, ignore) }
        else
          files << f
        end
      end
      dirs + files.sort
    end