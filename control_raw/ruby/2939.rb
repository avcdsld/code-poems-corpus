def with_restart_on_deadlock
      yield
    rescue ActiveRecord::StatementInvalid => exception
      if exception.message =~ /deadlock/i || exception.message =~ /database is locked/i
        ActiveSupport::Notifications.publish('deadlock_restart.double_entry', :exception => exception)

        raise ActiveRecord::RestartTransaction
      else
        raise
      end
    end