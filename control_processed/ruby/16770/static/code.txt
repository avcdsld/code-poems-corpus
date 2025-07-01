def sanitize_cookies(env)
      return unless env['HTTP_COOKIE']

      env['HTTP_COOKIE'] = env['HTTP_COOKIE']
        .split(/[;,] */n)
        .map { |cookie| sanitize_uri_encoded_string(cookie) }
        .join('; ')
    end