def server
      @server_mu.synchronize do
        @server ||= begin
          # For backward compatibility, we allow these options to be passed directly
          # in the Gruf::Server options, or via Gruf.rpc_server_options.
          server_options = {
            pool_size: options.fetch(:pool_size, Gruf.rpc_server_options[:pool_size]),
            max_waiting_requests: options.fetch(:max_waiting_requests, Gruf.rpc_server_options[:max_waiting_requests]),
            poll_period: options.fetch(:poll_period, Gruf.rpc_server_options[:poll_period]),
            pool_keep_alive: options.fetch(:pool_keep_alive, Gruf.rpc_server_options[:pool_keep_alive]),
            connect_md_proc: options.fetch(:connect_md_proc, Gruf.rpc_server_options[:connect_md_proc]),
            server_args: options.fetch(:server_args, Gruf.rpc_server_options[:server_args])
          }

          server = if @event_listener_proc
                     server_options[:event_listener_proc] = @event_listener_proc
                     Gruf::InstrumentableGrpcServer.new(server_options)
                   else
                     GRPC::RpcServer.new(server_options)
                   end

          @port = server.add_http2_port(@hostname, ssl_credentials)
          @services.each { |s| server.handle(s) }
          server
        end
      end
    end