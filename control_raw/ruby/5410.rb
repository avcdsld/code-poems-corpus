def find(path, id, params = {})
      response = get("/#{path.to_s.pluralize}/#{id}", params)
      trello_class = class_from_path(path)
      trello_class.parse response do |data|
        data.client = self
      end
    end