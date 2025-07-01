def login
      username = VoipfoneClient.configuration.username
      password = VoipfoneClient.configuration.password
      cookie_file = File.join(VoipfoneClient::TMP_FOLDER,"voipfone_client_cookies.yaml")

      # load existing cookies from the file on disk
      if File.exists?(cookie_file)
        @browser.cookie_jar.load(cookie_file)
      end

      # if we're authenticated at this point, we're done.
      return true if authenticated?

      # …otherwise we need to login to the service
      login_url = "#{VoipfoneClient::BASE_URL}/login.php?method=process"
      @browser.post(login_url,{"hash" => "urlHash", "login" => username, "password" => password})

      # If we're authenticated at this point, save the cookies and return true
      if authenticated?
        @browser.cookie_jar.save(cookie_file, session: true)
        return true
      # otherwise, we've tried to authenticate and failed, which means we have a 
      # bad username / password combo and it's time to raise an error.
      else
        raise NotAuthenticatedError, "Username or Password weren't accepted."
      end
    end