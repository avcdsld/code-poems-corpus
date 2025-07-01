def handle_cookies(file_path = nil)
      if file_path
        path = Pathname(file_path).expand_path
        
        if !File.exists?(file_path) && !File.writable?(path.dirname)
          raise ArgumentError, "Can't create file #{path} (permission error)"
        elsif File.exists?(file_path) && !File.writable?(file_path)
          raise ArgumentError, "Can't read or write file #{path} (permission error)"
        end
      else
        path = nil
      end
      
      # Apparently calling this with an empty string sets the cookie file,
      # but calling it with a path to a writable file sets that file to be
      # the cookie jar (new cookies are written there)
      add_cookie_file(path.to_s)
      
      self
    end