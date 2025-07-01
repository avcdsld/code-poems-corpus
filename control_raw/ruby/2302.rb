def log_events
      logger = Logging.logger[target.name]
      if (logs = value.dig('report', 'logs'))
        logs.each do |log|
          case log["level"]
          when 'err'
            logger.error(log['message'])
          when 'warn'
            logger.info(log['message'])
          when 'notice'
            logger.notice(log['message'])
          when 'info'
            logger.info(log['message'])
          else
            logger.debug(log["message"])
          end
        end
      end
    end