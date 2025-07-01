def handle_type(id_generator)
      if @type != 'AGGREGATE'
        # Generate the precondition for this population
        if @preconditions.length > 1 ||
           (@preconditions.length == 1 && @preconditions[0].conjunction != conjunction_code)
          @preconditions = [Precondition.new(id_generator.next_id, conjunction_code, @preconditions)]
        end
      else
        # Extract the data criteria this population references
        dc = handle_observation_criteria
        @preconditions = [Precondition.new(id_generator.next_id, nil, nil, false, HQMF2::Reference.new(dc.id))]
      end
    end