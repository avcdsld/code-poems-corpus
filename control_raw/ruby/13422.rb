def check_subdirectory(subpath)
      subdirectory = File.join(path, subpath)
      subdirectory if File.directory?(subdirectory)
    end