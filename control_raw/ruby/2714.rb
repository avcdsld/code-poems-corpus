def process_defs(exp, parent)
      inside_new_context(Context::SingletonMethodContext, exp, parent) do
        increase_statement_count_by(exp.body)
        process(exp)
      end
    end