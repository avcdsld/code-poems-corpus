def get(location, query_params = {})
      result = self.class.get(location, query_params)
      # FIXME: this is shit. should be based on on http response.
      if result['resultsPage']['error']
        msg = result['resultsPage']['error']['message']
        raise ResourceNotFound if msg =~ /not found/
        raise APIError.new(msg)
      end
      result
    end