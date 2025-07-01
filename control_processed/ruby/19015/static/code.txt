def expire_duration
      split_duration = @task.expires_after.split(".")
      duration = split_duration[0].to_i
      duration_units = split_duration[1]
      duration.send(duration_units)
    end