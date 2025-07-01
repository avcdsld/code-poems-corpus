def view(spec)
      results = CouchPotato::View::ViewQuery.new(
        couchrest_database,
        spec.design_document,
        {spec.view_name => {
          :map => spec.map_function,
          :reduce => spec.reduce_function
        }
        },
        ({spec.list_name => spec.list_function} unless spec.list_name.nil?),
        spec.lib,
        spec.language
      ).query_view!(spec.view_parameters)
      processed_results = spec.process_results results
      processed_results.each do |document|
        document.database = self if document.respond_to?(:database=)
      end if processed_results.respond_to?(:each)
      processed_results
    end