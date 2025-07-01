def try_get_io_from_logger(logger)
      logdev = logger.instance_eval { @logdev }
      if logdev.respond_to?(:dev)
        # ::Logger
        logdev.dev
      else
        # logdev is IO if DaemonLogger. otherwise unknown object including nil
        logdev
      end
    end