def redirect(url, opts = {})
      default_redirect_options = { :message => nil, :permanent => false }
      opts = default_redirect_options.merge(opts)

      url = handle_redirect_messages(url,opts)
      self.status = opts[:permanent] ? 301 : 302
      Merb.logger.info("Redirecting to: #{url} (#{self.status})")
      headers['Location'] = url
      "<html><body>You are being <a href=\"#{url}\">redirected</a>.</body></html>"
    end