def success(response)
      log.info "Parsing response as success..."

      case response['Content-Type']
      when /json/
        log.debug "Detected response as JSON"
        log.debug "Parsing response body as JSON"
        JSON.parse(response.body)
      else
        log.debug "Detected response as text/plain"
        response.body
      end
    end