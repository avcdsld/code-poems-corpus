def exec(sock, ver, path)   #:nodoc: internal use only
      if @body
        send_request_with_body sock, ver, path, @body
      elsif @body_stream
        send_request_with_body_stream sock, ver, path, @body_stream
      else
        write_header sock, ver, path
      end
    end