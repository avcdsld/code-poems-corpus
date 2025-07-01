def disconnect_from(network)
      connection = @connections.delete connection_to(network)
      connection.tap(&:stop).tap(&:join) unless connection.nil?
    end