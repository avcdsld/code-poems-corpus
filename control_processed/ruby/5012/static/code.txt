def connection
      @connection ||= self.class.connection_class.connect(
        url: config.solr.url,
        read_timeout: config.solr.read_timeout,
        open_timeout: config.solr.open_timeout,
        proxy: config.solr.proxy,
        update_format: config.solr.update_format || :xml
      )
    end