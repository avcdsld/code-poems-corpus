def refund(options = {})
      response = JSON.parse(@client.patch("items/#{send(:id)}/refund", options).body)
      @attributes = response['items']
      true
    end