def error(response)
      log.info "Parsing response as error..."

      case response['Content-Type']
      when /json/
        log.debug "Detected error response as JSON"
        log.debug "Parsing error response as JSON"
        message = JSON.parse(response.body)
      else
        log.debug "Detected response as text/plain"
        message = response.body
      end

      case response.code.to_i
      when 400
        raise Error::HTTPBadRequest.new(message: message)
      when 401
        raise Error::HTTPUnauthorizedRequest.new(message: message)
      when 403
        raise Error::HTTPForbiddenRequest.new(message: message)
      when 404
        raise Error::HTTPNotFound.new(message: message)
      when 405
        raise Error::HTTPMethodNotAllowed.new(message: message)
      when 406
        raise Error::HTTPNotAcceptable.new(message: message)
      when 504
        raise Error::HTTPGatewayTimeout.new(message: message)
      when 500..600
        raise Error::HTTPServerUnavailable.new
      else
        raise "I got an error #{response.code} that I don't know how to handle!"
      end
    end