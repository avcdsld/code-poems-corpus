def do_copy_in(path_map)
      path_map.each do |src_path, dst_path|
        if src_path != dst_path
          ::FileUtils.mkdir_p(::File.dirname(dst_path))
          ::FileUtils.cp(src_path, dst_path)
        end
      end
      true
    end