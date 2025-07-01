def reload!
      if links && links["self"]
        attrs = JSON.parse(connection.get(links["self"]).body)
        @attributes = OpenStruct.new(attrs)
        self
      else
        raise Unsplash::Error.new "Missing self link for #{self.class} with ID #{self.id}"
      end
    end