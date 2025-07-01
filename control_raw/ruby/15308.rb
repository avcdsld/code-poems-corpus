def get_object(objectID, attributes_to_retrieve = nil, request_options = {})
      attributes_to_retrieve = attributes_to_retrieve.join(',') if attributes_to_retrieve.is_a?(Array)
      if attributes_to_retrieve.nil?
        client.get(Protocol.object_uri(name, objectID, nil), :read, request_options)
      else
        client.get(Protocol.object_uri(name, objectID, { :attributes => attributes_to_retrieve }), :read, request_options)
      end
    end