def update(opts)
      opts = opts.merge(:option_id => self.option_id)
      Twocheckout::API.request(:post, 'products/update_option', opts)
      response = Twocheckout::API.request(:get, 'products/detail_option', opts)
      Option.new(response['option'][0])
    end