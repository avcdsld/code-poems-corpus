def complete(green, now)
      if ! started?
        raise Error, "Build #{id} not started"
      elsif completed?
        raise Error, "Build #{id} already completed"
      else
        update_attributes!(
          :green        => green,
          :completed_at => now,
          :output       => output_remote
        )
        Notifier.completed(self)
      end
    end