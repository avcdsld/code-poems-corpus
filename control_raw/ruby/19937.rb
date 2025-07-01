def upload(params = {})
      url = params.delete(:url)
      raise ArgumentError, 'You should pass :url parameter' unless url
      
      (params.delete(:files) || []).each_with_index do |file, index|
        key = "file#{index.succ}"
        params[key.to_sym] = file
      end
      
      files = {}
      params.each do |param_name, (file_path_or_io, file_type, file_path)|
        files[param_name] = Faraday::UploadIO.new(file_path_or_io, file_type, file_path)
      end
      
      API.connection.post(url, files).body
    end