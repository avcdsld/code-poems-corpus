def refresh!
      raise UnknownObject, self.name unless self.exists?
      h = Rudy::Metadata.get self.name
      return false if h.nil? || h.empty?
      obj = self.from_hash(h)
      obj.postprocess
      obj
    end