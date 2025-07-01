def activate_stream(id: nil, **args)
      connection_error(msg: 'Stream ID already exists') if @streams.key?(id)

      stream = Stream.new({ connection: self, id: id }.merge(args))

      # Streams that are in the "open" state, or either of the "half closed"
      # states count toward the maximum number of streams that an endpoint is
      # permitted to open.
      stream.once(:active) { @active_stream_count += 1 }
      stream.once(:close) do
        @active_stream_count -= 1

        # Store a reference to the closed stream, such that we can respond
        # to any in-flight frames while close is registered on both sides.
        # References to such streams will be purged whenever another stream
        # is closed, with a minimum of 15s RTT time window.
        @streams_recently_closed[id] = Time.now
        to_delete = @streams_recently_closed.select { |_, v| (Time.now - v) > 15 }
        to_delete.each do |stream_id|
          @streams.delete stream_id
          @streams_recently_closed.delete stream_id
        end
      end

      stream.on(:promise, &method(:promise)) if self.is_a? Server
      stream.on(:frame,   &method(:send))

      @streams[id] = stream
    end