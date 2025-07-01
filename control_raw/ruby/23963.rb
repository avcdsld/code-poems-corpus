def matchlist=(content)
      validate_list_content(content)
      @matchlist = case content 
      when :default then set_list_content(DEFAULT_MATCHLIST)
      else set_list_content(content)
      end
      @exceptionlist = set_list_content(content,folder: "exceptionlists") if content.class == Symbol and @exceptionlist.empty?
      @creative_matchlist = @matchlist.map {|list_item| use_creative_letters(list_item)}
    end