def new_files
      files = Set.new
      site.each_site_file { |item| files << item.destination(site.dest) }
      files
    end