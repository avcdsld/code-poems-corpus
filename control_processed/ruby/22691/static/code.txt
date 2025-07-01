def generalization_error_from_oob(oob_ids)
      return nil if (@structure.nil? || @individuals.nil? || @id_to_fenotype.nil?)
      oob_errors = {}
      oob_ids.each do |oobi|
        oob_prediction = Tree.traverse @structure, individuals[oobi].snp_list
        oob_errors[oobi] = Nimbus::LossFunctions.squared_difference oob_prediction, @id_to_fenotype[oobi]
      end
      @generalization_error = Nimbus::LossFunctions.average oob_ids, oob_errors
    end