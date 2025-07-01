def as_indexed_json(options={})
      self.as_json(
        include: { categories: { only: :title},
                   authors:    { methods: [:full_name, :department], only: [:full_name, :department] },
                   comments:   { only: :text }
                 })
    end