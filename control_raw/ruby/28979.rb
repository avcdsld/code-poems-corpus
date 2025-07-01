def check(text, options={})
      params = {
        :method => WebPurify::Constants.methods[:check],
        :text   => text
      }
      parsed = WebPurify::Request.query(text_request_base, @query_base, params.merge(options))
      return parsed[:found]=='1'
    end