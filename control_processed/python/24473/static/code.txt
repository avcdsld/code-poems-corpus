def xccdf(params):
    '''
    Run ``oscap xccdf`` commands on minions.
    It uses cp.push_dir to upload the generated files to the salt master
    in the master's minion files cachedir
    (defaults to ``/var/cache/salt/master/minions/minion-id/files``)

    It needs ``file_recv`` set to ``True`` in the master configuration file.

    CLI Example:

    .. code-block:: bash

        salt '*'  openscap.xccdf "eval --profile Default /usr/share/openscap/scap-yast2sec-xccdf.xml"
    '''
    params = shlex.split(params)
    policy = params[-1]

    success = True
    error = None
    upload_dir = None
    action = None
    returncode = None

    try:
        parser = _ArgumentParser()
        action = parser.parse_known_args(params)[0].action
        args, argv = _ArgumentParser(action=action).parse_known_args(args=params)
    except Exception as err:
        success = False
        error = six.text_type(err)

    if success:
        cmd = _XCCDF_MAP[action]['cmd_pattern'].format(args.profile, policy)
        tempdir = tempfile.mkdtemp()
        proc = Popen(
            shlex.split(cmd), stdout=PIPE, stderr=PIPE, cwd=tempdir)
        (stdoutdata, error) = proc.communicate()
        success = _OSCAP_EXIT_CODES_MAP[proc.returncode]
        returncode = proc.returncode
        if success:
            __salt__['cp.push_dir'](tempdir)
            shutil.rmtree(tempdir, ignore_errors=True)
            upload_dir = tempdir

    return dict(
        success=success,
        upload_dir=upload_dir,
        error=error,
        returncode=returncode)