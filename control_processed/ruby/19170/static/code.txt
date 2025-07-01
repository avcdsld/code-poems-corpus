def ship(opts)
      opts = opts.merge(:sale_id => self.sale_id)
      Twocheckout::API.request(:post, 'sales/mark_shipped', opts)
    end