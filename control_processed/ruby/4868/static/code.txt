def stat_sorted_tree_with_dependencies(dir)
      deps = Set.new([build_file_digest_uri(dir)])
      results = stat_sorted_tree(dir).map do |path, stat|
        deps << build_file_digest_uri(path) if stat.directory?
        [path, stat]
      end
      return results, deps
    end