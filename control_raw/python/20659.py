def run_and_track_hadoop_job(arglist, tracking_url_callback=None, env=None):
    """
    Runs the job by invoking the command from the given arglist.
    Finds tracking urls from the output and attempts to fetch errors using those urls if the job fails.
    Throws HadoopJobError with information about the error
    (including stdout and stderr from the process)
    on failure and returns normally otherwise.

    :param arglist:
    :param tracking_url_callback:
    :param env:
    :return:
    """
    logger.info('%s', subprocess.list2cmdline(arglist))

    def write_luigi_history(arglist, history):
        """
        Writes history to a file in the job's output directory in JSON format.
        Currently just for tracking the job ID in a configuration where
        no history is stored in the output directory by Hadoop.
        """
        history_filename = configuration.get_config().get('core', 'history-filename', '')
        if history_filename and '-output' in arglist:
            output_dir = arglist[arglist.index('-output') + 1]
            f = luigi.contrib.hdfs.HdfsTarget(os.path.join(output_dir, history_filename)).open('w')
            f.write(json.dumps(history))
            f.close()

    def track_process(arglist, tracking_url_callback, env=None):
        # Dump stdout to a temp file, poll stderr and log it
        temp_stdout = tempfile.TemporaryFile('w+t')
        proc = subprocess.Popen(arglist, stdout=temp_stdout, stderr=subprocess.PIPE, env=env, close_fds=True, universal_newlines=True)

        # We parse the output to try to find the tracking URL.
        # This URL is useful for fetching the logs of the job.
        tracking_url = None
        job_id = None
        application_id = None
        err_lines = []

        with HadoopRunContext() as hadoop_context:
            while proc.poll() is None:
                err_line = proc.stderr.readline()
                err_lines.append(err_line)
                err_line = err_line.strip()
                if err_line:
                    logger.info('%s', err_line)
                err_line = err_line.lower()
                tracking_url_match = TRACKING_RE.search(err_line)
                if tracking_url_match:
                    tracking_url = tracking_url_match.group('url')
                    try:
                        tracking_url_callback(tracking_url)
                    except Exception as e:
                        logger.error("Error in tracking_url_callback, disabling! %s", e)

                        def tracking_url_callback(x):
                            return None
                if err_line.find('running job') != -1:
                    # hadoop jar output
                    job_id = err_line.split('running job: ')[-1]
                if err_line.find('submitted hadoop job:') != -1:
                    # scalding output
                    job_id = err_line.split('submitted hadoop job: ')[-1]
                if err_line.find('submitted application ') != -1:
                    application_id = err_line.split('submitted application ')[-1]
                hadoop_context.job_id = job_id
                hadoop_context.application_id = application_id

        # Read the rest + stdout
        err = ''.join(err_lines + [an_err_line for an_err_line in proc.stderr])
        temp_stdout.seek(0)
        out = ''.join(temp_stdout.readlines())

        if proc.returncode == 0:
            write_luigi_history(arglist, {'job_id': job_id})
            return (out, err)

        # Try to fetch error logs if possible
        message = 'Streaming job failed with exit code %d. ' % proc.returncode
        if not tracking_url:
            raise HadoopJobError(message + 'Also, no tracking url found.', out, err)

        try:
            task_failures = fetch_task_failures(tracking_url)
        except Exception as e:
            raise HadoopJobError(message + 'Additionally, an error occurred when fetching data from %s: %s' %
                                 (tracking_url, e), out, err)

        if not task_failures:
            raise HadoopJobError(message + 'Also, could not fetch output from tasks.', out, err)
        else:
            raise HadoopJobError(message + 'Output from tasks below:\n%s' % task_failures, out, err)

    if tracking_url_callback is None:
        def tracking_url_callback(x): return None

    return track_process(arglist, tracking_url_callback, env)