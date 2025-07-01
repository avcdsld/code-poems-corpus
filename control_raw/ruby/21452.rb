def get_proxy_info_for_env
      parsed_uri = URI.parse(ENV['HTTP_PROXY'])
      if parsed_uri.scheme.to_s.downcase == 'http'
        return parsed_uri.host, parsed_uri.port, parsed_uri.user, parsed_uri.password
      else
        @logger.warn "Invalid protocol in ENV['HTTP_PROXY'] URI = #{ENV['HTTP_PROXY'].inspect} expecting 'http' got #{parsed_uri.scheme.inspect}"
        return
      end
    rescue Exception => e
      @logger.warn "Error parsing ENV['HTTP_PROXY'] with exception: #{e.message}"
      return
    end