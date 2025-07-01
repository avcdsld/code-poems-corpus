def strip_whitespace
      self.pattern           = pattern.strip unless pattern.nil?
      self.archive_directory = archive_directory.strip unless archive_directory.nil?
    end