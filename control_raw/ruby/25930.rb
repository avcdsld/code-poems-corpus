def upsert_smart_invite(body={})
      body[:event][:start] = encode_event_time(body[:event][:start])
      body[:event][:end] = encode_event_time(body[:event][:end])

      response = wrapped_request { api_key!.post("/v1/smart_invites", json_request_args(body)) }
      parse_json(SmartInviteResponse, nil, response)
    end