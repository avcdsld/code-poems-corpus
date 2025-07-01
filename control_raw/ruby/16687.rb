def run(sock)
      while true
        res = HTTPResponse.new(@config)
        req = HTTPRequest.new(@config)
        server = self
        begin
          timeout = @config[:RequestTimeout]
          while timeout > 0
            break if IO.select([sock], nil, nil, 0.5)
            timeout = 0 if @status != :Running
            timeout -= 0.5
          end
          raise HTTPStatus::EOFError if timeout <= 0
          raise HTTPStatus::EOFError if sock.eof?
          req.parse(sock)
          res.request_method = req.request_method
          res.request_uri = req.request_uri
          res.request_http_version = req.http_version
          res.keep_alive = req.keep_alive?
          server = lookup_server(req) || self
          if callback = server[:RequestCallback]
            callback.call(req, res)
          elsif callback = server[:RequestHandler]
            msg = ":RequestHandler is deprecated, please use :RequestCallback"
            @logger.warn(msg)
            callback.call(req, res)
          end
          server.service(req, res)
        rescue HTTPStatus::EOFError, HTTPStatus::RequestTimeout => ex
          res.set_error(ex)
        rescue HTTPStatus::Error => ex
          @logger.error(ex.message)
          res.set_error(ex)
        rescue HTTPStatus::Status => ex
          res.status = ex.code
        rescue StandardError => ex
          @logger.error(ex)
          res.set_error(ex, true)
        ensure
          if req.request_line
            if req.keep_alive? && res.keep_alive?
              req.fixup()
            end
            res.send_response(sock)
            server.access_log(@config, req, res)
          end
        end
        break if @http_version < "1.1"
        break unless req.keep_alive?
        break unless res.keep_alive?
      end
    end