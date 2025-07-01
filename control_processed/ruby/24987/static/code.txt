def flush(ops = queue)
      operations, callbacks = ops.transpose
      logging(operations) do
        ensure_connected do |conn|
          conn.write(operations)
          replies = conn.receive_replies(operations)

          replies.zip(callbacks).map do |reply, callback|
            callback ? callback[reply] : reply
          end.last
        end
      end
    ensure
      ops.clear
    end