def get_running_jobs(opts):
    '''
    Return the running jobs on the master
    '''

    ret = []
    proc_dir = os.path.join(opts['cachedir'], 'proc')
    if not os.path.isdir(proc_dir):
        return ret
    for fn_ in os.listdir(proc_dir):
        path = os.path.join(proc_dir, fn_)
        data = read_proc_file(path, opts)
        if not data:
            continue
        if not is_pid_healthy(data['pid']):
            continue
        ret.append(data)
    return ret