def roll_required?
      mtime = copy_file_mtime
      return false if mtime && (Time.now - mtime) < 180

      # check if max size has been exceeded
      s = @size ? ::File.size(filename) > @size : false

      # check if max age has been exceeded
      a = sufficiently_aged?

      return (s || a)
    end