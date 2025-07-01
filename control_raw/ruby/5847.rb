def read_with_retry_cursor(session, server_selector, view, &block)
      read_with_retry(session, server_selector) do |server|
        result = yield server
        Cursor.new(view, result, server, session: session)
      end
    end