def create_stack(options = {})
      resp = @client.create_stack(options)
      Stack.new(
        id: resp.data.stack_id,
        client: @client
      )
    end