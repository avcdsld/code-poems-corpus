def post(params)
      base_params = {
        format: 'json'
      }
      base_params[:assert] = @assertion.to_s if @assertion
      params = base_params.merge(params)
      header = {}
      if defined? @custom_agent
        header['User-Agent'] = @custom_agent
      else
        header['User-Agent'] = @logged_in ? "#{@name}/MediaWiki::Butt" : 'NotLoggedIn/MediaWiki::Butt'
      end

      response = JSON.parse(@client.post(@uri, params, header).body)

      if @assertion
        code = response.dig('error', 'code')
        fail MediaWiki::Butt::NotLoggedInError.new(response['error']['info']) if code == 'assertuserfailed'
        fail MediaWiki::Butt::NotBotError.new(response['error']['info']) if code == 'assertbotfailed'
      end
      response
    end