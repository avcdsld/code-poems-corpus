def write(file = find_file, force: false, format: :auto)
      if file && ::File.exist?(file)
        if !force
          raise WriteError, "File `#{file}` already exists. " \
                            'Use :force option to overwrite.'
        elsif !::File.writable?(file)
          raise WriteError, "Cannot write to #{file}."
        end
      end

      if file.nil?
        dir = @location_paths.empty? ? Dir.pwd : @location_paths.first
        file = ::File.join(dir, "#{filename}#{@extname}")
      end

      content = marshal(file, @settings, format: format)
      ::File.write(file, content)
    end