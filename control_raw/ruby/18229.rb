def start
      @connection.connect
      @publisher.broadcast(:online)
      @subscriber.subscribe

      EM.add_periodic_timer(1) { heartbeat }

      at_exit do
        @publisher.broadcast(:offline)
        @sessions.delete_all(@id)
      end
    end