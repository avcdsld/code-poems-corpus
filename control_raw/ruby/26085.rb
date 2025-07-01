def set_cookie(name, value, expires)
      options = expires.is_a?(Hash) ? expires : {:expires => expires}
      cookies.set_cookie(name, value, options)
    end