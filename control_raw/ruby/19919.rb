def init_access_log
      return if access_log_dest.nil?

      log = ::Logging.logger['access_log']
      pattern = ::Logging.layouts.pattern(:pattern => ACCESS_LOG_PATTERN)

      log.add_appenders(
        ::Logging.appenders.rolling_file(access_log_dest,
          :level => :debug,
          :age => 'daily',
          :layout => pattern)
        )

      log
    end