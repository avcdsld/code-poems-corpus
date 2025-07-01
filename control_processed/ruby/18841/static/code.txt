def add(url, code = nil, options = nil)
      code_for(url) || insert(url, get_code(url, code, options))
    end