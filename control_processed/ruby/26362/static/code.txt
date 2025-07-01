def execute(objects, negate)
      method = negate ? :reject : :select

      objects.send(method) { |object| has_tags?(object, tags) }
    end