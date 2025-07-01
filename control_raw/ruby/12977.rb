def receive(timeout = nil, &block)
      loop do
        message = @receivers.receive(timeout, &block)
        return message unless message.is_a?(SystemEvent)

        handle_system_event(message)
      end
    end