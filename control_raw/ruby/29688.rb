def nested_directory_map(paths)
      directories = {}

      options[:patterns].product(paths).each do |pattern, path|
        next unless (matches = path.match(pattern))

        target = options[:output] || File.dirname(path)
        if (subpath = matches[1])
          target = File.join(target, File.dirname(subpath)).gsub(/\/\.$/, '')
        end

        (directories[target] ||= []) << path
      end

      directories
    end