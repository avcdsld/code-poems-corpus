def formatted_content
      formatted_content = content
      formatted_content.each do |k,v|
        if v.is_a?(String) and v =~ /\n/
          formatted_content[k] = to_markdown(v)
        end
      end
      
      formatted_content
    end