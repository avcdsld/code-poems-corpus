def rename!(*arguments)
      Hash[*arguments.flatten].each_pair do |from,to|
        if fields.has_key?(from) && !fields.has_key?(to)
          fields[to] = fields[from]
          fields.delete(from)
        end
      end
      self
    end