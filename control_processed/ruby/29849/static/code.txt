def start
      return if @state != :stopped

      Service.start(@options[:ampq_uri], @options[:threadpool_size])
      EM.run do

        @channel = AMQP::Channel.new(@@connection)

        @channel.on_error do |ch, channel_close|
          message = "Channel exception: [#{channel_close.reply_code}] #{channel_close.reply_text}"
          puts message
          raise message
        end

        @channel.prefetch(@options[:prefetch])
        @channel.auto_recovery = true

        @service_queue = @channel.queue( @service_queue_name, {:durable => true})
        @service_queue.subscribe({:ack => true}) do |metadata, payload|
          payload = JSON.parse(payload)
          process_service_queue_message(metadata, payload)
        end

        response_queue = @channel.queue(@response_queue_name, {:exclusive => true, :auto_delete => true})
        response_queue.subscribe({}) do |metadata, payload|
          payload = JSON.parse(payload)
          process_response_queue_message(metadata, payload)
        end

        @channel.default_exchange.on_return do |basic_return, frame, payload|
          payload = JSON.parse(payload)
          process_returned_message(basic_return, frame.properties, payload)
        end

        # RESOURCES HANDLE
        @resources_exchange = @channel.topic("resources.exchange", {:durable => true})
        @resources_exchange.on_return do |basic_return, frame, payload|
          payload = JSON.parse(payload)
          process_returned_message(basic_return, frame.properties, payload)
        end

        bound_resources = 0
        for resource_path in @options[:resource_paths]
          binding_key = "#{path_to_routing_key(resource_path)}.#"
          @service_queue.bind(@resources_exchange, :key => binding_key) {
            bound_resources += 1
          }
        end
        begin
          # simple loop to wait for the resources to be bound
          sleep(0.01)
        end until bound_resources == @options[:resource_paths].length

        @state = :started
      end
    end