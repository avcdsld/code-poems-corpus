def log(page = 1, per_page = 20, order_by = :request_time, order_dir = :desc)
      params = {
        :page => page,
        :per_page => per_page,
        :order_by => order_by,
        :order_dir => order_dir
      }
      DataSift.request(:GET, 'push/log', @config, params)
    end