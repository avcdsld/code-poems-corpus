def new_clients_for(*nodes)
      nodes.map do |node|
        host, port = node.split(':')
        opts = {:host => host, :port => port}
        opts.update(:db => @db) if @db
        opts.update(:password => @password) if @password
        client = Redis.new(@redis_client_options.merge(opts))
        if @namespace
          client = Redis::Namespace.new(@namespace, :redis => client)
        end
        @node_addresses[client] = node
        client
      end
    end