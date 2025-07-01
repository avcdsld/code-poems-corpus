def search_disjunctive_faceting(query, disjunctive_facets, params = {}, refinements = {}, request_options = {})
      raise ArgumentError.new('Argument "disjunctive_facets" must be a String or an Array') unless disjunctive_facets.is_a?(String) || disjunctive_facets.is_a?(Array)
      raise ArgumentError.new('Argument "refinements" must be a Hash of Arrays') if !refinements.is_a?(Hash) || !refinements.select { |k, v| !v.is_a?(Array) }.empty?

      # extract disjunctive facets & associated refinements
      disjunctive_facets = disjunctive_facets.split(',') if disjunctive_facets.is_a?(String)
      disjunctive_refinements = {}
      refinements.each do |k, v|
        disjunctive_refinements[k] = v if disjunctive_facets.include?(k) || disjunctive_facets.include?(k.to_s)
      end

      # build queries
      queries = []
      ## hits + regular facets query
      filters = []
      refinements.to_a.each do |k, values|
        r = values.map { |v| "#{k}:#{v}" }
        if disjunctive_refinements[k.to_s] || disjunctive_refinements[k.to_sym]
          # disjunctive refinements are ORed
          filters << r
        else
          # regular refinements are ANDed
          filters += r
        end
      end
      queries << params.merge({ :index_name => self.name, :query => query, :facetFilters => filters })
      ## one query per disjunctive facet (use all refinements but the current one + hitsPerPage=1 + single facet)
      disjunctive_facets.each do |disjunctive_facet|
        filters = []
        refinements.each do |k, values|
          if k.to_s != disjunctive_facet.to_s
            r = values.map { |v| "#{k}:#{v}" }
            if disjunctive_refinements[k.to_s] || disjunctive_refinements[k.to_sym]
              # disjunctive refinements are ORed
              filters << r
            else
              # regular refinements are ANDed
              filters += r
            end
          end
        end
        queries << params.merge({
          :index_name => self.name,
          :query => query,
          :page => 0,
          :hitsPerPage => 1,
          :attributesToRetrieve => [],
          :attributesToHighlight => [],
          :attributesToSnippet => [],
          :facets => disjunctive_facet,
          :facetFilters => filters,
          :analytics => false
        })
      end
      answers = client.multiple_queries(queries, { :request_options => request_options })

      # aggregate answers
      ## first answer stores the hits + regular facets
      aggregated_answer = answers['results'][0]
      ## others store the disjunctive facets
      aggregated_answer['disjunctiveFacets'] = {}
      answers['results'].each_with_index do |a, i|
        next if i == 0
        a['facets'].each do |facet, values|
          ## add the facet to the disjunctive facet hash
          aggregated_answer['disjunctiveFacets'][facet] = values
          ## concatenate missing refinements
          (disjunctive_refinements[facet.to_s] || disjunctive_refinements[facet.to_sym] || []).each do |r|
            if aggregated_answer['disjunctiveFacets'][facet][r].nil?
              aggregated_answer['disjunctiveFacets'][facet][r] = 0
            end
          end
        end
      end

      aggregated_answer
    end