def remove_schedule(name)
      SidekiqScheduler::RedisManager.remove_job_schedule(name)
      SidekiqScheduler::RedisManager.add_schedule_change(name)
    end