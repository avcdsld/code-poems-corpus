def start(url, now)
      if started?
        raise Error, "Build #{id} already started"
      elsif completed?
        raise Error, "Build #{id} already completed"
      else
        update_attributes!(:url => url, :started_at => now)
        Notifier.started(self)
      end
    end