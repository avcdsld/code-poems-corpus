def put(path, options = {})
      ext = options[:ext] || File.extname(path)
      path = path.to_s
      resp = http_post("/v1/#{appkey}",
                       File.open(path.start_with?('/') ? path : fpath(path)).read,
                       :params => {
                         :suffix => ext,
                         :simple_name => options[:simple_name] || 0
                       },
                       :accept => :json)

      json = JSON.parse(resp)
      json && json['TFS_FILE_NAME']
    end