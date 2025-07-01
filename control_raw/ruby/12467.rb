def path_to_module(path, base=nil)
      if base
        path = ::File.expand_path(path, base)
        raise PoisePython::Error.new("Path #{path} is not inside base path #{base}") unless path.start_with?(base)
        path = path[base.length+1..-1]
      end
      path = path[0..-4] if path.end_with?('.py')
      path.gsub(/#{::File::SEPARATOR}/, '.')
    end