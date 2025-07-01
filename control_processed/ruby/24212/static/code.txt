def which(cmd, paths: search_paths)
      if file_with_path?(cmd)
        return cmd if executable_file?(cmd)
        extensions.each do |ext|
          exe = ::File.join(cmd, ext)
          return ::File.absolute_path(exe) if executable_file?(exe)
        end
        return nil
      end

      paths.each do |path|
        if file_with_exec_ext?(cmd)
          exe = ::File.join(path, cmd)
          return ::File.absolute_path(exe) if executable_file?(exe)
        end
        extensions.each do |ext|
          exe = ::File.join(path, "#{cmd}#{ext}")
          return ::File.absolute_path(exe) if executable_file?(exe)
        end
      end
      nil
    end