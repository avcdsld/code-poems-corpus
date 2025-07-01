def add_index(table_name, column_name, options = {})
      column_names = Array(column_name)
      index_name   = index_name(table_name, :column => column_names)

      if Hash === options # legacy support, since this param was a string
        index_type = options[:unique] ? "UNIQUE" : ""
        index_name = options[:name] || index_name
        index_method = options[:spatial] ? 'USING GIST' : ""
      else
        index_type = options
      end
      quoted_column_names = column_names.map { |e| quote_column_name(e) }.join(", ")
      execute "CREATE #{index_type} INDEX #{quote_column_name(index_name)} ON #{quote_table_name(table_name)} #{index_method} (#{quoted_column_names})"
    end