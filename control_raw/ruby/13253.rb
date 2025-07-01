def job_is_a_rocket_job
      klass = job_class
      return if job_class_name.nil? || klass&.ancestors&.include?(RocketJob::Job)
      errors.add(:job_class_name, "Job #{job_class_name} must be defined and inherit from RocketJob::Job")
    end