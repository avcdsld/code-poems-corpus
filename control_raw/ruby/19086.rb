def exclude_from_index(entity, boolean)
      entity.properties.to_h.each_key do |value|
        entity.exclude_from_indexes! value, boolean
      end
    end