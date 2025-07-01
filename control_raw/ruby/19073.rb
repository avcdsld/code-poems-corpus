def load(*paths)
      paths.flatten.each do |path|
        window.load(path.to_s)
      end
      self
    end