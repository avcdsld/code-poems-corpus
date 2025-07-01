def start
      @signal_to_stop = false

      start_listener

      begin
        start_consumer_loop
      rescue Kafka::ProcessingError, Phobos::AbortError
        # Abort is an exception to prevent the consumer from committing the offset.
        # Since "listener" had a message being retried while "stop" was called
        # it's wise to not commit the batch offset to avoid data loss. This will
        # cause some messages to be reprocessed
        instrument('listener.retry_aborted', listener_metadata) do
          log_info('Retry loop aborted, listener is shutting down', listener_metadata)
        end
      end
    ensure
      stop_listener
    end