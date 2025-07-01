def reconnect(url=nil, user=nil, pass=nil, opts={})
    @connection_pool.disconnect!
    connect(url, user, pass, opts)
  end