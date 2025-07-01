def solr_name(field_name, *opts)
      index_type, args = if opts.first.kind_of? Hash
        [:stored_searchable, opts.first]
      elsif opts.empty?
        [:stored_searchable, {type: :text}]
      else
        [opts[0], opts[1] || {type: :string}]
      end

      indexer(index_type).name_and_converter(field_name, args).first
    end