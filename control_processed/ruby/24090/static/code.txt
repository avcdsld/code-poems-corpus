def load_path(path)
      path = path.to_s
      check_error_string do
        @path = Pathname.new(path)
        load_path_impl(path)
      end
      self
    end