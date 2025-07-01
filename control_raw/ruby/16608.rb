def timestamp
      if File.exist?(name)
        File.mtime(name.to_s)
      else
        Rake::EARLY
      end
    end