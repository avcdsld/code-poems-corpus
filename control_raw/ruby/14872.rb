def basic_authorize(user, password)
      browser.set_http_auth(user, password)
      credentials = ["#{user}:#{password}"].pack('m*').strip
      add_header('Authorization', "Basic #{credentials}")
    end