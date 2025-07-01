def waiter(duration=2, max=240, logger=STDOUT, msg=nil, bells=0, &check)
      # TODO: Move to Drydock. [ed-why?]
      raise "The waiter needs a block!" unless check
      duration = 1 if duration < 1
      max = duration*2 if max < duration
      dot = '.'
      begin
        if msg && logger
          logger.print msg 
          logger.flush
        end
        Timeout::timeout(max) do
          while !check.call
            sleep duration
            logger.print dot if logger.respond_to?(:print)
            logger.flush if logger.respond_to?(:flush)
          end
        end
      rescue Timeout::Error => ex
        retry if Annoy.pose_question(" Keep waiting?\a ", /yes|y|ya|sure|you bet!/i, logger)
        return false
      end
      
      if msg && logger
        logger.puts
        logger.flush
      end
      
      Rudy::Utils.bell(bells, logger)
      true
    end