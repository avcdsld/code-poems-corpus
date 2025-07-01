def multi_search(body = nil, params = nil)
      if block_given?
        params, body = (body || {}), nil
        yield msearch_obj = MultiSearch.new(self, params)
        msearch_obj.call
      else
        raise "multi_search request body cannot be nil" if body.nil?
        params ||= {}

        response = self.post "{/index}{/type}/_msearch", params.merge(body: body, action: "msearch", rest_api: "msearch")
        response.body
      end
    end