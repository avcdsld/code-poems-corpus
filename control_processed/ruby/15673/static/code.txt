def from_file(filename)
      if %w{ .yml .yaml }.include?(File.extname(filename))
        from_yaml(filename)
      elsif File.extname(filename) == ".json"
        from_json(filename)
      elsif File.extname(filename) == ".toml"
        from_toml(filename)
      else
        instance_eval(IO.read(filename), filename, 1)
      end
    end