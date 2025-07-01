def has_callouts?
      parser = REXML::Parsers::PullParser.new(File.new(@docbook_file))
      while parser.has_next?
        el = parser.pull
        if el.start_element? and (el[0] == "calloutlist" or el[0] == "co")
          return true
        end  
      end
      return false
    end