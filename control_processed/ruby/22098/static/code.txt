def make_positive_entry
      negated_criteria = []
      data_criteria_index_lookup = []
      # Find the criteria that are negated
      # At the same time build a hash of all criteria and their code_list_id, definition, status, and negation status
      @data_criteria.each_with_index do |criterion, source_index|
        negated_criteria << criterion if criterion.negation
        data_criteria_index_lookup << [criterion.code_list_id, criterion.definition, criterion.status, criterion.negation]
      end

      negated_criteria.each do |criterion|
        # Check if there is a criterion with the same OID, definition and status BUT that isn't negated
        unless data_criteria_index_lookup.include?([criterion.code_list_id, criterion.definition, criterion.status, false])
          spoofed_positive_instance = criterion.clone
          spoofed_positive_instance.make_criterion_positive
          @data_criteria << spoofed_positive_instance
          sdc = spoofed_positive_instance.clone
          sdc.id += '_source'
          @source_data_criteria << sdc
        end
      end

    end