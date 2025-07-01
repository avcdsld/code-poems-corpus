def extensions(path_ext = ENV['PATHEXT'])
      return [''] unless path_ext
      path_ext.split(::File::PATH_SEPARATOR).select { |part| part.include?('.') }
    end