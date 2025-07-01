public synchronized void insertSchedule(final Schedule s) {
    final Schedule exist = this.scheduleIdentityPairMap.get(s.getScheduleIdentityPair());
    if (s.updateTime()) {
      try {
        if (exist == null) {
          this.loader.insertSchedule(s);
          internalSchedule(s);
        } else {
          s.setScheduleId(exist.getScheduleId());
          this.loader.updateSchedule(s);
          internalSchedule(s);
        }
      } catch (final ScheduleManagerException e) {
        logger.error(e);
      }
    } else {
      logger
          .error("The provided schedule is non-recurring and the scheduled time already passed. "
              + s.getScheduleName());
    }
  }