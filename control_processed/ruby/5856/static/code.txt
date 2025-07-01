def distinct(field_name, filter = nil, options = {})
      View.new(self, filter || {}, options).distinct(field_name, options)
    end