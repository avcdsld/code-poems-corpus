def run(hits = @hits, prediction = @prediction)
      raise NotEnoughHitsError if hits.length < opt[:min_blast_hits]
      raise unless prediction.is_a?(Query) && hits[0].is_a?(Query)

      start = Time.now

      hits_lengths = hits.map { |x| x.length_protein.to_i }
                         .sort { |a, b| a <=> b }

      no_of_hits   = hits_lengths.length
      median       = hits_lengths.median.round
      query_length = prediction.length_protein
      mean         = hits_lengths.mean.round

      smallest_hit = hits_lengths[0]
      largest_hit  = hits_lengths[-1]

      if hits_lengths.standard_deviation <= 5
        msg = ''
        percentage = 100
      else
        if query_length < median
          extreme_hits = hits_lengths.find_all { |x| x < query_length }.length
          percentage   = ((extreme_hits.to_f / no_of_hits) * 100).round
          msg          = 'too&nbsp;short'
        else
          extreme_hits = hits_lengths.find_all { |x| x > query_length }.length
          percentage   = ((extreme_hits.to_f / no_of_hits) * 100).round
          msg          = 'too&nbsp;long'
        end
      end

      msg = '' if percentage >= THRESHOLD

      @validation_report = LengthRankValidationOutput.new(@short_header,
                                                          @header, @description,
                                                          msg, query_length,
                                                          no_of_hits, median,
                                                          mean, smallest_hit,
                                                          largest_hit,
                                                          extreme_hits,
                                                          percentage)
      @validation_report.run_time = Time.now - start
      @validation_report
    rescue NotEnoughHitsError
      @validation_report = ValidationReport.new('Not enough evidence', :warning,
                                                @short_header, @header,
                                                @description)
    rescue StandardError
      @validation_report = ValidationReport.new('Unexpected error', :error,
                                                @short_header, @header,
                                                @description)
      @validation_report.errors.push 'Unexpected Error'
    end