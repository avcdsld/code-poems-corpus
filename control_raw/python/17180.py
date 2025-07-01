def sge_submit(nslave, worker_args, worker_envs):
    """
      customized submit script, that submit nslave jobs, each must contain args as parameter
      note this can be a lambda function containing additional parameters in input
      Parameters
         nslave number of slave process to start up
         args arguments to launch each job
              this usually includes the parameters of master_uri and parameters passed into submit
    """
    env_arg = ','.join(['%s=\"%s\"' % (k, str(v)) for k, v in worker_envs.items()])
    cmd = 'qsub -cwd -t 1-%d -S /bin/bash' % nslave
    if args.queue != 'default':
        cmd += '-q %s' % args.queue
    cmd += ' -N %s ' % args.jobname
    cmd += ' -e %s -o %s' % (args.logdir, args.logdir)
    cmd += ' -pe orte %d' % (args.vcores)
    cmd += ' -v %s,PATH=${PATH}:.' % env_arg
    cmd += ' %s %s' % (runscript, ' '.join(args.command + worker_args))
    print cmd
    subprocess.check_call(cmd, shell = True)
    print 'Waiting for the jobs to get up...'