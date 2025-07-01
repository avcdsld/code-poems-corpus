def find_many(trello_class, path, params = {})
      response = get(path, params)
      trello_class.parse_many response do |data|
        data.client = self
      end
    end