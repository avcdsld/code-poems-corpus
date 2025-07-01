def get_response(request)
      begin
        data = @transport.recv(@max_bytes)
        message = Message.decode(data, @mib)
        response = message.pdu
      end until request.request_id == response.request_id
      response
    end