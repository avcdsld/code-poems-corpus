def to_expr( key, value, field = nil )
      Sequel.expr( predicates[key, value, field] )
    end