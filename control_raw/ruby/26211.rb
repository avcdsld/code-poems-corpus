def featured(options = {}, &block)
      params = {}

      if options[:hls]
        params[:hls] = true
      end

      return @query.connection.accumulate(
        :path => 'streams/featured',
        :params => params,
        :json => 'featured',
        :sub_json => 'stream',
        :create => -> hash { Stream.new(hash, @query) },
        :limit => options[:limit],
        :offset => options[:offset],
        &block
      )
    end