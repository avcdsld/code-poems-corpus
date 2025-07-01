def call env
      response = @app.call env
      return response unless @paths === env['PATH_INFO']
      
      status, headers, body = response
      return response unless headers['Content-Type'] == nil or headers['Content-Type'].start_with?('text/html')
      newbody = []
      body.each { |str| newbody << str }
      newbody = newbody.join('')
      newbody = InlineStyle.process(newbody, {:stylesheets_path => "./build/"}.merge(@opts))
      headers['Content-Length'] = Rack::Utils.bytesize(newbody).to_s
      [status, headers, [newbody]]
    end