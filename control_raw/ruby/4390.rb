def process_token(type, token)
      # Remove the "Bot " prefix if it exists
      token = token[4..-1] if token.start_with? 'Bot '

      token = 'Bot ' + token unless type == :user
      token
    end