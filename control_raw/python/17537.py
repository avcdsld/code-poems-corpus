def scheduler(ctx, xmlrpc, xmlrpc_host, xmlrpc_port,
              inqueue_limit, delete_time, active_tasks, loop_limit, fail_pause_num,
              scheduler_cls, threads, get_object=False):
    """
    Run Scheduler, only one scheduler is allowed.
    """
    g = ctx.obj
    Scheduler = load_cls(None, None, scheduler_cls)

    kwargs = dict(taskdb=g.taskdb, projectdb=g.projectdb, resultdb=g.resultdb,
                  newtask_queue=g.newtask_queue, status_queue=g.status_queue,
                  out_queue=g.scheduler2fetcher, data_path=g.get('data_path', 'data'))
    if threads:
        kwargs['threads'] = int(threads)

    scheduler = Scheduler(**kwargs)
    scheduler.INQUEUE_LIMIT = inqueue_limit
    scheduler.DELETE_TIME = delete_time
    scheduler.ACTIVE_TASKS = active_tasks
    scheduler.LOOP_LIMIT = loop_limit
    scheduler.FAIL_PAUSE_NUM = fail_pause_num

    g.instances.append(scheduler)
    if g.get('testing_mode') or get_object:
        return scheduler

    if xmlrpc:
        utils.run_in_thread(scheduler.xmlrpc_run, port=xmlrpc_port, bind=xmlrpc_host)
    scheduler.run()