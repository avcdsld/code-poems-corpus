def read_loop(set_input_stream_done, is_client: true)
      return enum_for(:read_loop,
                      set_input_stream_done,
                      is_client: is_client) unless block_given?
      GRPC.logger.debug('bidi-read-loop: starting')
      begin
        count = 0
        # queue the initial read before beginning the loop
        loop do
          GRPC.logger.debug("bidi-read-loop: #{count}")
          count += 1
          batch_result = read_using_run_batch

          # handle the next message
          if batch_result.nil? || batch_result.message.nil?
            GRPC.logger.debug("bidi-read-loop: null batch #{batch_result}")

            if is_client
              batch_result = @call.run_batch(RECV_STATUS_ON_CLIENT => nil)
              @call.status = batch_result.status
              @call.trailing_metadata = @call.status.metadata if @call.status
              GRPC.logger.debug("bidi-read-loop: done status #{@call.status}")
              batch_result.check_status
            end

            GRPC.logger.debug('bidi-read-loop: done reading!')
            break
          end

          res = @unmarshal.call(batch_result.message)
          yield res
        end
      rescue StandardError => e
        GRPC.logger.warn('bidi: read-loop failed')
        GRPC.logger.warn(e)
        raise e
      ensure
        set_input_stream_done.call
      end
      GRPC.logger.debug('bidi-read-loop: finished')
      # Make sure that the write loop is done before finishing the call.
      # Note that blocking is ok at this point because we've already received
      # a status
      @enq_th.join if is_client
    end