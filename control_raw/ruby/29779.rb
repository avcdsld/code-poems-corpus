def connect!
      @connection = HTTParty.post(File.join(url, "rest/user/login"), body: credentials_hash )
      @cookies['Cookie'] = @connection.headers['set-cookie']
      @connection.code
    end