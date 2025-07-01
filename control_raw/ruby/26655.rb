def read_content(dir, magic_dir, matcher)
      @site.reader.get_entries(dir, magic_dir).map do |entry|
        next unless entry =~ matcher
        path = @site.in_source_dir(File.join(dir, magic_dir, entry))
        Document.new(path, {
          :site       => @site,
          :collection => @site.posts,
        })
      end.reject(&:nil?)
    end