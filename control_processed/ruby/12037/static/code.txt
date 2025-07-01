def enqueue_job(job_config, time = Time.now)
      config = prepare_arguments(job_config.dup)

      if config.delete('include_metadata')
        config['args'] = arguments_with_metadata(config['args'], scheduled_at: time.to_f)
      end

      if active_job_enqueue?(config['class'])
        SidekiqScheduler::Utils.enqueue_with_active_job(config)
      else
        SidekiqScheduler::Utils.enqueue_with_sidekiq(config)
      end
    end