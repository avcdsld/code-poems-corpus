def create_stack(options = {})
      resp = @client.create_stack(options)
      Stack.new(
        name: options[:stack_name],
        client: @client
      )
    end