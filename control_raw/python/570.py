def setJobGroup(self, groupId, description, interruptOnCancel=False):
        """
        Assigns a group ID to all the jobs started by this thread until the group ID is set to a
        different value or cleared.

        Often, a unit of execution in an application consists of multiple Spark actions or jobs.
        Application programmers can use this method to group all those jobs together and give a
        group description. Once set, the Spark web UI will associate such jobs with this group.

        The application can use L{SparkContext.cancelJobGroup} to cancel all
        running jobs in this group.

        >>> import threading
        >>> from time import sleep
        >>> result = "Not Set"
        >>> lock = threading.Lock()
        >>> def map_func(x):
        ...     sleep(100)
        ...     raise Exception("Task should have been cancelled")
        >>> def start_job(x):
        ...     global result
        ...     try:
        ...         sc.setJobGroup("job_to_cancel", "some description")
        ...         result = sc.parallelize(range(x)).map(map_func).collect()
        ...     except Exception as e:
        ...         result = "Cancelled"
        ...     lock.release()
        >>> def stop_job():
        ...     sleep(5)
        ...     sc.cancelJobGroup("job_to_cancel")
        >>> suppress = lock.acquire()
        >>> suppress = threading.Thread(target=start_job, args=(10,)).start()
        >>> suppress = threading.Thread(target=stop_job).start()
        >>> suppress = lock.acquire()
        >>> print(result)
        Cancelled

        If interruptOnCancel is set to true for the job group, then job cancellation will result
        in Thread.interrupt() being called on the job's executor threads. This is useful to help
        ensure that the tasks are actually stopped in a timely manner, but is off by default due
        to HDFS-1208, where HDFS may respond to Thread.interrupt() by marking nodes as dead.
        """
        self._jsc.setJobGroup(groupId, description, interruptOnCancel)