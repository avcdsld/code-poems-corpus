def serialize
      {
        "job_class"  => self.class.name,
        "job_id"     => job_id,
        "provider_job_id" => provider_job_id,
        "queue_name" => queue_name,
        "priority"   => priority,
        "arguments"  => serialize_arguments_if_needed(arguments),
        "executions" => executions,
        "exception_executions" => exception_executions,
        "locale"     => I18n.locale.to_s,
        "timezone"   => Time.zone.try(:name),
        "enqueued_at" => Time.now.utc.iso8601
      }
    end