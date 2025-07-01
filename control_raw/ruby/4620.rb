def handle_sd_rmn_sy(tokens, options)
      new_tokens = [tokens[1], tokens[0], tokens[2]]
      time_tokens = tokens.last(tokens.size - 3)
      handle_rmn_sd_sy(new_tokens + time_tokens, options)
    end