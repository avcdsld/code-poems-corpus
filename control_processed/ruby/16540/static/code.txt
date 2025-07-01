def receive_responses
      connection_closed = false
      until connection_closed
        synchronize do
          @exception = nil
        end
        begin
          resp = get_response
        rescue Exception => e
          synchronize do
            @sock.close
            @exception = e
          end
          break
        end
        unless resp
          synchronize do
            @exception = EOFError.new("end of file reached")
          end
          break
        end
        begin
          synchronize do
            case resp
            when TaggedResponse
              @tagged_responses[resp.tag] = resp
              @tagged_response_arrival.broadcast
              if resp.tag == @logout_command_tag
                return
              end
            when UntaggedResponse
              record_response(resp.name, resp.data)
              if resp.data.instance_of?(ResponseText) &&
                  (code = resp.data.code)
                record_response(code.name, code.data)
              end
              if resp.name == "BYE" && @logout_command_tag.nil?
                @sock.close
                @exception = ByeResponseError.new(resp)
                connection_closed = true
              end
            when ContinuationRequest
              @continuation_request_arrival.signal
            end
            @response_handlers.each do |handler|
              handler.call(resp)
            end
          end
        rescue Exception => e
          @exception = e
          synchronize do
            @tagged_response_arrival.broadcast
            @continuation_request_arrival.broadcast
          end
        end
      end
      synchronize do
        @receiver_thread_terminating = true
        @tagged_response_arrival.broadcast
        @continuation_request_arrival.broadcast
        if @idle_done_cond
          @idle_done_cond.signal
        end
      end
    end