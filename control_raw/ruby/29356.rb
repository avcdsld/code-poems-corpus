def send
      if @trans.sent
        raise "Batch has already been sent!"
      end
      @trans.sent = true

      requests = @trans.requests

      if requests.length < 1
        raise RpcException.new(-32600, "Batch cannot be empty")
      end

      # Send request batch to server
      resp_list = @parent.trans.request(requests)
      
      # Build a hash for the responses so we can re-order them
      # in request order.
      sorted    = [ ]
      by_req_id = { }
      resp_list.each do |resp|
        by_req_id[resp["id"]] = resp
      end

      # Iterate through the requests in the batch and assemble
      # the sorted result array
      requests.each do |req|
        id = req["id"]
        resp = by_req_id[id]
        if !resp
          msg = "No result for request id: #{id}"
          resp = { "id" => id, "error" => { "code"=>-32603, "message" => msg } }
        end
        sorted << RpcResponse.new(req, resp)
      end

      return sorted
    end