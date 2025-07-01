def backfill_derived_code_lists
      data_criteria_by_id = {}
      @data_criteria.each {|criteria| data_criteria_by_id[criteria.id] = criteria}
      @data_criteria.each do |criteria|
        if (criteria.derived_from)
          derived_from = data_criteria_by_id[criteria.derived_from]
          criteria.definition = derived_from.definition
          criteria.status = derived_from.status
          criteria.code_list_id = derived_from.code_list_id
        end
      end
    end