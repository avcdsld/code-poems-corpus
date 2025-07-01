def calling_cookbook_path(options, kaller)
      File.expand_path(File.join(calling_cookbook_root(options, kaller), '..'))
    end