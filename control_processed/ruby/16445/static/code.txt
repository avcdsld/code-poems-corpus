def update_into_table(table=nil,values=nil,condition=nil)
    raise ArgumentError if !table || !values
    query = nil
    vals = []
    if condition
        quests_set, vals_set = make_set_params(values)
        quests_where,vals_where = Database.make_where_params(condition,'AND')
        query = "UPDATE \"#{table}\" SET #{quests_set} WHERE #{quests_where}"
        vals = vals_set + vals_where
    else
        quests, vals = make_set_params(values)
        query = "UPDATE \"#{table}\" SET #{quests}"
    end

    execute_sql query, vals
  end