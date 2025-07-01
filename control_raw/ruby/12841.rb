def once(event, &block)
      add_listener(event) do |*args, &callback|
        block.call(*args, &callback)
        :delete
      end
    end