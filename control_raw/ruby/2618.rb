def read filename
      return @current if @current && @current.filename == filename
      raise FileNotFoundError, "File not found: #{filename}" unless workspace.has_file?(filename)
      workspace.source(filename)
    end