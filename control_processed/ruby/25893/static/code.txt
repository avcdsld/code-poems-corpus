def login(retries = 2)
      options = {
        'body' => {
          'userName' => @user,
          'password' => @password,
          'authLoginDomain' => @domain
        }
      }
      response = rest_post('/rest/login-sessions', options)
      body = response_handler(response)
      return body['sessionID'] if body['sessionID']
      raise ConnectionError, "\nERROR! Couldn't log into OneView server at #{@url}. Response: #{response}\n#{response.body}"
    rescue StandardError => e
      raise e unless retries > 0
      @logger.debug 'Failed to log in to OneView. Retrying...'
      return login(retries - 1)
    end