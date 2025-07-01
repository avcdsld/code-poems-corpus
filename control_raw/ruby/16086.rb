def build_request(action, url, headers, options = {})
      # If the Expect header isn't set uploads are really slow
      headers['Expect'] ||= ''

      Request.new.tap do |req|
        req.action                 = action
        req.headers                = self.headers.merge headers
        req.automatic_content_encoding = options.fetch :automatic_content_encoding, self.automatic_content_encoding
        req.timeout                = options.fetch :timeout,               self.timeout
        req.connect_timeout        = options.fetch :connect_timeout,       self.connect_timeout
        req.dns_cache_timeout      = options.fetch :dns_cache_timeout,     self.dns_cache_timeout
        req.low_speed_time         = options.fetch :low_speed_time,        self.low_speed_time
        req.low_speed_limit        = options.fetch :low_speed_limit,       self.low_speed_limit
        req.force_ipv4             = options.fetch :force_ipv4,            self.force_ipv4
        req.max_redirects          = options.fetch :max_redirects,         self.max_redirects
        req.username               = options.fetch :username,              self.username
        req.password               = options.fetch :password,              self.password
        req.proxy                  = options.fetch :proxy,                 self.proxy
        req.proxy_type             = options.fetch :proxy_type,            self.proxy_type
        req.auth_type              = options.fetch :auth_type,             self.auth_type
        req.insecure               = options.fetch :insecure,              self.insecure
        req.ssl_version            = options.fetch :ssl_version,           self.ssl_version
        req.http_version           = options.fetch :http_version,          self.http_version
        req.cacert                 = options.fetch :cacert,                self.cacert
        req.ignore_content_length  = options.fetch :ignore_content_length, self.ignore_content_length
        req.buffer_size            = options.fetch :buffer_size,           self.buffer_size
        req.download_byte_limit    = options.fetch :download_byte_limit,   self.download_byte_limit
        req.progress_callback      = options.fetch :progress_callback,     self.progress_callback
        req.multipart              = options[:multipart]
        req.upload_data            = options[:data]
        req.file_name              = options[:file]

        base_url = self.base_url.to_s
        url = url.to_s
        raise ArgumentError, "Empty URL" if base_url.empty? && url.empty?
        uri = URI.parse(base_url.empty? ? url : File.join(base_url, url))
        query = uri.query.to_s.split('&')
        query += options[:query].is_a?(Hash) ? Util.build_query_pairs_from_hash(options[:query]) : options[:query].to_s.split('&')
        uri.query = query.join('&')
        uri.query = nil if uri.query.empty?
        url = uri.to_s
        req.url = url
      end
    end