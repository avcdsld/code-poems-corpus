def extract_group_data_criteria_tree(conjunction, preconditions, type, parent_id)
      
      children = []
      preconditions.each do |precondition|
        if (precondition.comparison?) 
          if (precondition.reference.id == HQMF::Document::MEASURE_PERIOD_ID)
            children << measure_period_criteria
          else
            children << v2_data_criteria_by_id[precondition.reference.id]
          end
        else
          converted_conjunction = convert_grouping_conjunction(precondition.conjunction_code) 
          children << extract_group_data_criteria_tree(converted_conjunction, precondition.preconditions, type, parent_id)
        end
      end
      
      # if we have just one child element, just return it.  An AND or OR of a single item is not useful.
      if (children.size > 1)
        build_group_data_criteria(children, type, parent_id, conjunction)
      else
        children.first
      end
      
    end