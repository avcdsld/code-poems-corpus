def update_all(updates)
      raise ArgumentError, "Empty list of attributes to change" if updates.blank?

      if eager_loading?
        relation = apply_join_dependency
        return relation.update_all(updates)
      end

      stmt = Arel::UpdateManager.new
      stmt.table(arel.join_sources.empty? ? table : arel.source)
      stmt.key = arel_attribute(primary_key)
      stmt.take(arel.limit)
      stmt.offset(arel.offset)
      stmt.order(*arel.orders)
      stmt.wheres = arel.constraints

      if updates.is_a?(Hash)
        if klass.locking_enabled? &&
            !updates.key?(klass.locking_column) &&
            !updates.key?(klass.locking_column.to_sym)
          attr = arel_attribute(klass.locking_column)
          updates[attr.name] = _increment_attribute(attr)
        end
        stmt.set _substitute_values(updates)
      else
        stmt.set Arel.sql(klass.sanitize_sql_for_assignment(updates, table.name))
      end

      @klass.connection.update stmt, "#{@klass} Update All"
    end