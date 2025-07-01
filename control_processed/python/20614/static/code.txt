def run(self):
        """
        Returns True if all scheduled tasks were executed successfully.
        """
        logger.info('Running Worker with %d processes', self.worker_processes)

        sleeper = self._sleeper()
        self.run_succeeded = True

        self._add_worker()

        while True:
            while len(self._running_tasks) >= self.worker_processes > 0:
                logger.debug('%d running tasks, waiting for next task to finish', len(self._running_tasks))
                self._handle_next_task()

            get_work_response = self._get_work()

            if get_work_response.worker_state == WORKER_STATE_DISABLED:
                self._start_phasing_out()

            if get_work_response.task_id is None:
                if not self._stop_requesting_work:
                    self._log_remote_tasks(get_work_response)
                if len(self._running_tasks) == 0:
                    self._idle_since = self._idle_since or datetime.datetime.now()
                    if self._keep_alive(get_work_response):
                        six.next(sleeper)
                        continue
                    else:
                        break
                else:
                    self._handle_next_task()
                    continue

            # task_id is not None:
            logger.debug("Pending tasks: %s", get_work_response.n_pending_tasks)
            self._run_task(get_work_response.task_id)

        while len(self._running_tasks):
            logger.debug('Shut down Worker, %d more tasks to go', len(self._running_tasks))
            self._handle_next_task()

        return self.run_succeeded