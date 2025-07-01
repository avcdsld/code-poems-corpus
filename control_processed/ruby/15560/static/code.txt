def add(type, info)
    path, info = type_info(type, :path), force_case(info)
    reply = json_parse_reply(@key_style, *json_post(@target, path, info,
        headers))
    fake_client_id(reply) if type == :client # hide client reply, not quite scim
    reply
  end