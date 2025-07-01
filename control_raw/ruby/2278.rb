def post_filter(params = nil, &block)
      params = Filters.new(&block).__render__ if block
      chain { criteria.update_post_filters params }
    end