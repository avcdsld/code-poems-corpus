def accounts(id = nil, opts = {})
      id ? Account.load(self, id) : Account.all(self, opts)
    end