def get_rule(objectID, request_options = {})
      client.get(Protocol.rule_uri(name, objectID), :read, request_options)
    end