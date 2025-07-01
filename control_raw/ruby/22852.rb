def index_text
      term_generator = Xapian::TermGenerator.new
      term_generator.database = @database.writer
      term_generator.document = @xapian_doc
      if XapianDb::Config.stemmer
        term_generator.stemmer  = XapianDb::Config.stemmer
        term_generator.stopper  = XapianDb::Config.stopper if XapianDb::Config.stopper
        # Enable the creation of a spelling dictionary if the database is not in memory
        term_generator.set_flags Xapian::TermGenerator::FLAG_SPELLING if @database.is_a? XapianDb::PersistentDatabase
      end

      # Index the primary key as a unique term
      @xapian_doc.add_term("Q#{@obj.xapian_id}")

      # Index the class with the field name
      term_generator.index_text("#{@obj.class}".downcase, 1, "XINDEXED_CLASS")
      @xapian_doc.add_term("C#{@obj.class}")

      @blueprint.indexed_method_names.each do |method|
        options = @blueprint.options_for_indexed_method method
        if options.block
          obj = @obj.instance_eval(&options.block)
        else
          obj = @obj.send(method)
        end
        unless obj.nil?
          values = get_values_to_index_from obj
          values.each do |value|
            terms = value.to_s.downcase
            terms = @blueprint.preprocess_terms.call(terms) if @blueprint.preprocess_terms
            terms = split(terms) if XapianDb::Config.term_splitter_count > 0 && !options.no_split
            # Add value with field name
            term_generator.index_text(terms, options.weight, "X#{method.upcase}") if options.prefixed
            # Add value without field name
            term_generator.index_text(terms, options.weight)
          end
        end
      end

      terms_to_ignore = @xapian_doc.terms.select{ |term| term.term.length < XapianDb::Config.term_min_length }
      terms_to_ignore.each { |term| @xapian_doc.remove_term term.term }
    end