def exec_insert(sql, name = nil, binds = [], pk = nil, sequence_name = nil)
      exec_query(sql, name, binds)
    end