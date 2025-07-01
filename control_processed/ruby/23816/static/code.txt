def build_from_file(file)
      dir = File.dirname(file)
      string = IO.read(file)
      build_from_string(string, dir)
    end