def each(&block)
      if WebsocketRails.synchronize?
        users_hash = Synchronization.all_users || return
        users_hash.each do |identifier, user_json|
          connection = remote_connection_from_json(identifier, user_json)
          block.call(connection) if block
        end
      else
        users.each do |_, connection|
          block.call(connection) if block
        end
      end
    end