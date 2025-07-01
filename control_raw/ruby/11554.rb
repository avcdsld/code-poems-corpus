def header(name, data)
      fail(Mailgun::ParameterError, 'Header name for message must be specified') if name.to_s.empty?
      begin
        jsondata = make_json data
        set_single("h:#{name}", jsondata)
      rescue Mailgun::ParameterError
        set_single("h:#{name}", data)
      end
    end