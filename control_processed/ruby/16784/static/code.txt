def update(params={})
      instance_variable_set(:@summary, params[:summary])
      instance_variable_set(:@location, params[:location])
      instance_variable_set(:@description, params[:description])
      instance_variable_set(:@time_zone, params[:time_zone])

      response =
        send_calendar_request(
                              "/#{@id}", 
                              :put, 
                              {
                               summary: @summary,
                               location: @location,
                               description: @description,
                               timeZone: @time_zone,
                              }.to_json
                             )
      @raw = JSON.parse(response.body)
      self
    end