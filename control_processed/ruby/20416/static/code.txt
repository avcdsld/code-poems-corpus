def fetch_attachment(name)
      raise ArgumentError, "doc must be saved" unless self.rev
      raise ArgumentError, "doc.database required to put_attachment" unless database
      database.fetch_attachment(self, name)
    end