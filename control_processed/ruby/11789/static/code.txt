def version_from_file
      if File.exist?(Rails.root.join("REVISION"))
        File.read(Rails.root.join("REVISION")).chomp
      end
    end