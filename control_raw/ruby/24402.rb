def url=(vco_url)
      url = URI.parse(vco_url)
      url.path = '/vco/api'
      @url = url.to_s
    end