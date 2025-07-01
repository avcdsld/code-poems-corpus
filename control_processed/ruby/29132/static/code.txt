def modify_content(source, content, replace_value)
      file = File.read(source)
      replace = file.gsub(/#{content}/, replace_value)
      File.open(source, "w"){|f|
        f.puts replace       
      }
    end