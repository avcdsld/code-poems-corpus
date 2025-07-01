def add_to_many(activity_data, feeds)
      data = {
        :feeds => feeds,
        :activity => activity_data
      }
      signature = Stream::Signer.create_jwt_token('feed', '*', @api_secret, '*')
      make_request(:post, '/feed/add_to_many/', signature, {}, data)
    end