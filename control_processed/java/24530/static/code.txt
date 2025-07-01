public synchronized boolean unscheduleJob(final String jobName, final String groupName) throws
      SchedulerException {
    return this.scheduler.deleteJob(new JobKey(jobName, groupName));
  }