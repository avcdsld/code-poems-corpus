def to_s
      if self.scheme == nil && self.path != nil && !self.path.empty? &&
          self.path =~ NORMPATH
        raise InvalidURIError,
          "Cannot assemble URI string with ambiguous path: '#{self.path}'"
      end
      @uri_string ||= begin
        uri_string = String.new
        uri_string << "#{self.scheme}:" if self.scheme != nil
        uri_string << "//#{self.authority}" if self.authority != nil
        uri_string << self.path.to_s
        uri_string << "?#{self.query}" if self.query != nil
        uri_string << "##{self.fragment}" if self.fragment != nil
        uri_string.force_encoding(Encoding::UTF_8)
        uri_string
      end
    end