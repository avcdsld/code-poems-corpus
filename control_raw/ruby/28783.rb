def gen_salt
      chars = []
      8.times { chars << SALT_CHARS[SecureRandom.random_number(SALT_CHARS.size)] }
      chars.join('')
    end