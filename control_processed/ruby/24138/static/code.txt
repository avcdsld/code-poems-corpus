def create_table(table_name, column_definition = {})
      cols = column_definition.to_a.map { |a| a.join(' ') }.join(', ')
      stmt = %{CREATE TABLE "#{table_name}" (#{cols})}
      execute(stmt)
    end