def get_image_refs
      parser = REXML::Parsers::PullParser.new(File.new(@docbook_file))
      image_refs = []
      while parser.has_next?
        el = parser.pull
        if el.start_element? and (el[0] == "imagedata" or el[0] == "graphic")
          image_refs << el[1]['fileref'] 
        end  
      end
      return image_refs
    end