def delete_rsrc(rsrc, xml = nil)
      validate_connected
      raise MissingDataError, 'Missing :rsrc' if rsrc.nil?

      # payload?
      return delete_with_payload rsrc, xml if xml

      # delete the resource
      @last_http_response = @cnx[rsrc].delete
    rescue RestClient::ExceptionWithResponse => e
      handle_http_error e
    end