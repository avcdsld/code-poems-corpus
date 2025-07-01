def trace(queue_names=self.queues.keys, tracer=nil, &block)
      queues_to_trace = self.queues.slice(*queue_names)
      queues_to_trace.each do |name, opts|
        opts.merge! :durable => false, :auto_delete => true, :amqp_name => queue_name_for_tracing(opts[:amqp_name])
      end
      tracer ||=
        lambda do |msg|
          puts "-----===== new message =====-----"
          puts "SERVER: #{msg.server}"
          puts "HEADER: #{msg.header.attributes[:headers].inspect}"
          puts "EXCHANGE: #{msg.header.method.exchange}"
          puts "KEY: #{msg.header.method.routing_key}"
          puts "MSGID: #{msg.msg_id}"
          puts "DATA: #{msg.data}"
        end
      register_handler(queue_names){|msg| tracer.call msg }
      listen_queues(queue_names, &block)
    end