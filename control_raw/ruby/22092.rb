def delete_endpoint(endpoint_id)
      endpoint = EndPoint.new({:id => endpoint_id}, @client)
      endpoint.domain_id = id
      endpoint.delete()
    end