def parse!( obligation )
      @current_obligation = obligation
      @join_table_joins = Set.new
      obligation_conditions[@current_obligation] ||= {}
      follow_path( obligation )

      rebuild_condition_options!
      rebuild_join_options!
    end