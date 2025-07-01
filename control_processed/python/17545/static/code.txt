def bench(ctx, fetcher_num, processor_num, result_worker_num, run_in, total, show,
          taskdb_bench, message_queue_bench, all_bench):
    """
    Run Benchmark test.
    In bench mode, in-memory sqlite database is used instead of on-disk sqlite database.
    """
    from pyspider.libs import bench
    from pyspider.webui import bench_test  # flake8: noqa

    ctx.obj['debug'] = False
    g = ctx.obj
    if result_worker_num == 0:
        g['processor2result'] = None

    if run_in == 'subprocess' and os.name != 'nt':
        run_in = utils.run_in_subprocess
    else:
        run_in = utils.run_in_thread

    all_test = not taskdb_bench and not message_queue_bench and not all_bench

    # test taskdb
    if all_test or taskdb_bench:
        bench.bench_test_taskdb(g.taskdb)
    # test message queue
    if all_test or message_queue_bench:
        bench.bench_test_message_queue(g.scheduler2fetcher)
    # test all
    if not all_test and not all_bench:
        return

    project_name = 'bench'

    def clear_project():
        g.taskdb.drop(project_name)
        g.resultdb.drop(project_name)

    clear_project()

    # disable log
    logging.getLogger().setLevel(logging.ERROR)
    logging.getLogger('scheduler').setLevel(logging.ERROR)
    logging.getLogger('fetcher').setLevel(logging.ERROR)
    logging.getLogger('processor').setLevel(logging.ERROR)
    logging.getLogger('result').setLevel(logging.ERROR)
    logging.getLogger('webui').setLevel(logging.ERROR)
    logging.getLogger('werkzeug').setLevel(logging.ERROR)

    try:
        threads = []

        # result worker
        result_worker_config = g.config.get('result_worker', {})
        for i in range(result_worker_num):
            threads.append(run_in(ctx.invoke, result_worker,
                                  result_cls='pyspider.libs.bench.BenchResultWorker',
                                  **result_worker_config))

        # processor
        processor_config = g.config.get('processor', {})
        for i in range(processor_num):
            threads.append(run_in(ctx.invoke, processor,
                                  processor_cls='pyspider.libs.bench.BenchProcessor',
                                  **processor_config))

        # fetcher
        fetcher_config = g.config.get('fetcher', {})
        fetcher_config.setdefault('xmlrpc_host', '127.0.0.1')
        for i in range(fetcher_num):
            threads.append(run_in(ctx.invoke, fetcher,
                                  fetcher_cls='pyspider.libs.bench.BenchFetcher',
                                  **fetcher_config))

        # webui
        webui_config = g.config.get('webui', {})
        webui_config.setdefault('scheduler_rpc', 'http://127.0.0.1:%s/'
                                % g.config.get('scheduler', {}).get('xmlrpc_port', 23333))
        threads.append(run_in(ctx.invoke, webui, **webui_config))

        # scheduler
        scheduler_config = g.config.get('scheduler', {})
        scheduler_config.setdefault('xmlrpc_host', '127.0.0.1')
        scheduler_config.setdefault('xmlrpc_port', 23333)
        threads.append(run_in(ctx.invoke, scheduler,
                              scheduler_cls='pyspider.libs.bench.BenchScheduler',
                              **scheduler_config))
        scheduler_rpc = connect_rpc(ctx, None,
                                    'http://%(xmlrpc_host)s:%(xmlrpc_port)s/' % scheduler_config)

        for _ in range(20):
            if utils.check_port_open(23333):
                break
            time.sleep(1)

        scheduler_rpc.newtask({
            "project": project_name,
            "taskid": "on_start",
            "url": "data:,on_start",
            "fetch": {
                "save": {"total": total, "show": show}
            },
            "process": {
                "callback": "on_start",
            },
        })

        # wait bench test finished
        while True:
            time.sleep(1)
            if scheduler_rpc.size() == 0:
                break
    finally:
        # exit components run in threading
        for each in g.instances:
            each.quit()

        # exit components run in subprocess
        for each in threads:
            if hasattr(each, 'terminate'):
                each.terminate()
            each.join(1)

        clear_project()