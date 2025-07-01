def post(options)
      payload = {
        username: @options['name'],
        channel:  @options['channel']
      }.merge(options)
      payload[:channel] = payload[:channel].gsub(/^#?/, '#') #slack api needs leading # on channel
      request = Net::HTTP::Post.new(@uri.request_uri)
      request.set_form_data(payload: payload.to_json)
      @http.request(request)
      return nil # so as not to trigger text in outgoing webhook reply
    end