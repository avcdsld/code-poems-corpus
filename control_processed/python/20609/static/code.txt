def _add_task(self, *args, **kwargs):
        """
        Call ``self._scheduler.add_task``, but store the values too so we can
        implement :py:func:`luigi.execution_summary.summary`.
        """
        task_id = kwargs['task_id']
        status = kwargs['status']
        runnable = kwargs['runnable']
        task = self._scheduled_tasks.get(task_id)
        if task:
            self._add_task_history.append((task, status, runnable))
            kwargs['owners'] = task._owner_list()

        if task_id in self._batch_running_tasks:
            for batch_task in self._batch_running_tasks.pop(task_id):
                self._add_task_history.append((batch_task, status, True))

        if task and kwargs.get('params'):
            kwargs['param_visibilities'] = task._get_param_visibilities()

        self._scheduler.add_task(*args, **kwargs)

        logger.info('Informed scheduler that task   %s   has status   %s', task_id, status)