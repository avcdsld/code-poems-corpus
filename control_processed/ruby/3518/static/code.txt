def create_measure_period_v1_data_criteria(doc,measure_period,v1_data_criteria_by_id)

      attributes = doc[:attributes]
      attributes.keys.each {|key| attributes[key.to_s] = attributes[key]}
      
      measure_period_key = attributes['MEASUREMENT_PERIOD'][:id]
      measure_start_key = attributes['MEASUREMENT_START_DATE'][:id]
      measure_end_key = attributes['MEASUREMENT_END_DATE'][:id]
      
      @measure_period_v1_keys = {measure_start: measure_start_key, measure_end: measure_end_key, measure_period: measure_period_key}
      
      type = 'variable'
      code_list_id,negation_code_list_id,property,status,field_values,effective_time,inline_code_list,children_criteria,derivation_operator,temporal_references,subset_operators=nil
      
      #####
      ##
      ######### SET MEASURE PERIOD
      ##
      #####
      
      measure_period_id = HQMF::Document::MEASURE_PERIOD_ID
      value = measure_period
      measure_criteria = HQMF::DataCriteria.new(measure_period_id,measure_period_id,nil,measure_period_id,code_list_id,children_criteria,derivation_operator,measure_period_id,status,
                                                value,field_values,effective_time,inline_code_list, false, nil, temporal_references,subset_operators,nil,nil)
      
      # set the measure period data criteria for all measure period keys
      v1_data_criteria_by_id[measure_period_key] = measure_criteria
      v1_data_criteria_by_id[measure_start_key] = measure_criteria
      v1_data_criteria_by_id[measure_end_key] = measure_criteria
      @measure_period_criteria = measure_criteria
      
    end