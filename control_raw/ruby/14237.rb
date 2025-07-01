def to_options(options = {})
      options.merge(
        wsHost:       socket_options[:host],
        wsPort:       socket_options[:port],
        cluster:      "us-east-1",
        disableStats: disable_stats
      )
    end