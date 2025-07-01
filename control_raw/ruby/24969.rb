def update(params)
      raise ArgumentError, "Only Hash parameter can be passed to table update method" unless params.is_a?(Hash)
      where = params.delete(:where)

      table_proc = TableProcedure.new(@schema, self, :update)
      table_proc.add_set_arguments(params)
      table_proc.add_where_arguments(where) if where
      call = ProcedureCall.new(table_proc, table_proc.argument_values)
      call.exec
    end