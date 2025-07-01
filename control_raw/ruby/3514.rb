def handle_derived_specific_occurrences
      return unless @definition == 'derived'

      # remove "_source" from source data critera. It gets added in in SpecificOccurrenceAndSource but
      # when it gets added we have not yet determined the definition of the data criteria so we cannot
      # skip adding it.  Determining the definition before SpecificOccurrenceAndSource processes doesn't
      # work because we need to know if it is a specific occurrence to be able to figure out the definition
      @source_data_criteria = @source_data_criteria.gsub("_source",'') if @source_data_criteria

      # Adds a child if none exists (specifically the source criteria)
      @children_criteria << @source_data_criteria if @children_criteria.empty?
      return if @children_criteria.length != 1 ||
                (@source_data_criteria.present? && @children_criteria.first != @source_data_criteria)
      # if child.first is nil, it will be caught in the second statement
      reference_criteria = @data_criteria_references[@children_criteria.first]
      return if reference_criteria.nil?
      @is_derived_specific_occurrence_variable = true # easier to track than all testing all features of these cases
      @subset_operators ||= reference_criteria.subset_operators
      @derivation_operator ||= reference_criteria.derivation_operator
      @description = reference_criteria.description
      @variable = reference_criteria.variable
    end