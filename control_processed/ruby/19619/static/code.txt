def parse
      begin
        @parser.parse(@source)
        @feature = @builder.ast
        return nil if @feature.nil? # Nothing matched
        
        # The parser used the following keywords when parsing the feature
        # @feature.language = @parser.i18n_language.get_code_keywords.map {|word| word }
        
      rescue Gherkin::ParserError => e
        e.message.insert(0, "#{@file}: ")
        warn e
      end
      
      self
    end