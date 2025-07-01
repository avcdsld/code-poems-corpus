def get_more
      with_retry(session.cluster) do
        reply = @node.get_more @database, @collection, @cursor_id, request_limit
        @limit -= reply.count if limited?
        @cursor_id = reply.cursor_id
        reply.documents
      end
    end