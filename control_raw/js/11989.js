function _killAll() {
    var k,
        jobs = __extend(_jobs, _runningJobs, _waitingJobs);

    // Take every jobs and push them into the _doneJobs object:
    if (_parameters.history)
      for (k in jobs) {
        jobs[k].status = 'done';
        _doneJobs.push(jobs[k]);

        if (typeof jobs[k].end === 'function')
          jobs[k].end();
      }

    // Reinitialize the different jobs lists:
    _jobs = {};
    _waitingJobs = {};
    _runningJobs = {};
    _sortedByPriorityJobs = [];

    // In case some jobs are added right after the kill:
    _isRunning = false;

    return this;
  }