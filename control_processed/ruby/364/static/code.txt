def in_cache_dir(*paths)
      paths.reduce(cache_dir) do |base, path|
        Jekyll.sanitized_path(base, path)
      end
    end