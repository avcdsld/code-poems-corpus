def respond(response)
      no_body = @status < 200 || STATUS_WITH_NO_ENTITY_BODY[@status]
      write_status(response)
      write_headers(response)
      if @hijack
        @hijack.call(response.net_socket)
        return
      end
      if no_body
        response.end
      else
        if @body.respond_to?(:to_path)
          response.send_file(@body.to_path)
        else
          write_body(response)
          response.end
        end
      end
    rescue NativeException => e
      puts e
    ensure
      @body.close if @body.respond_to?(:close)
    end