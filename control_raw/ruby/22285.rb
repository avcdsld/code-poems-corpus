def make_payment(options = {})
      response = JSON.parse(@client.patch("items/#{send(:id)}/make_payment", options).body)
      @attributes = response['items']
      true
    end