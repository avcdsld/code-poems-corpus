def find(*ids, parent: nil)
      expects_array = ids.first.is_a?(Array)
      ids = ids.flatten.compact.uniq.map(&:to_i)

      case ids.size
      when 0
        raise EntityError, "Couldn't find #{name} without an ID"
      when 1
        entity = find_entity(ids.first, parent)
        model_entity = from_entity(entity)
        expects_array ? [model_entity].compact : model_entity
      else
        lookup_results = find_all_entities(ids, parent)
        from_entities(lookup_results.all)
      end
    end