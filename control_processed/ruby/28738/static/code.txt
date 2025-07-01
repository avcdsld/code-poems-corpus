def call( field_predicate, value, field = nil )
      unless respond_to? field_predicate
        define_name_predicate field_predicate, value, field
      end
      send field_predicate, value
    end