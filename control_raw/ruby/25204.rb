def onMessage(message)
      begin
        if @message_count
          @message_count += 1
          @last_time     = Time.now
        end
        logger.measure_debug('Message processed') do
          @proc.call message
        end
      rescue SyntaxError, NameError => exc
        logger.error "Ignoring poison message:\n#{message.inspect}", exc
      rescue StandardError => exc
        logger.error "Ignoring poison message:\n#{message.inspect}", exc
      rescue Exception => exc
        logger.error "Ignoring poison message:\n#{message.inspect}", exc
      end
    end