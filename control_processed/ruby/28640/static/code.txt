def gallery_list_all
      # ToDo: Research why Typhoeus works better than Faraday for this endpoint
      request = Typhoeus::Request.new(
        "#{Kairos::Configuration::GALLERY_LIST_ALL}",
        method: :post,
        headers: { "Content-Type" => "application/x-www-form-urlencoded",
                   "app_id"       => "#{@app_id}",
                   "app_key"      => "#{@app_key}" }
      )
      response = request.run
      JSON.parse(response.body) rescue "INVALID_JSON: #{response.body}"
    end