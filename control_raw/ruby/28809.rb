def read_file
      json_string = ''
      if ApiExplorer::use_file
        json_path = ApiExplorer::json_path
        json_string = File.read(json_path)
      else
        json_string = ApiExplorer::json_string
      end
       
      @methods = JSON.parse(json_string)["methods"]
    end