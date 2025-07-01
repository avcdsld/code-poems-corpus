def server
    reply = json_get(target, '/login', key_style)
    return reply if reply && (reply[:prompts] || reply['prompts'])
    raise BadResponse, "Invalid response from target #{target}"
  end