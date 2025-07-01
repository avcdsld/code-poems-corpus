def retrieve_static_files(dir, dot_static_files)
      site.static_files.concat(StaticFileReader.new(site, dir).read(dot_static_files))
    end