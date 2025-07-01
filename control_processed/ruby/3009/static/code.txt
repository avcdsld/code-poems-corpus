def sign_out(authenticatable_class)
      key = cookie_name(authenticatable_class)
      cookies.encrypted.permanent[key] = {value: nil}
      cookies.delete(key)
      true
    end