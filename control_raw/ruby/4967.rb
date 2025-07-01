def update!(opts={})
      response = Hubspot::Connection.post_json(LIST_PATH, params: { list_id: @id }, body: opts)
      self.send(:assign_properties, response)
      self
    end