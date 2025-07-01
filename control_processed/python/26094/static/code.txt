def sls(name, mods=None, **kwargs):
    '''
    Apply the states defined by the specified SLS modules to the running
    container

    .. versionadded:: 2016.11.0

    The container does not need to have Salt installed, but Python is required.

    name
        Container name or ID

    mods : None
        A string containing comma-separated list of SLS with defined states to
        apply to the container.

    saltenv : base
        Specify the environment from which to retrieve the SLS indicated by the
        `mods` parameter.

    pillarenv
        Specify a Pillar environment to be used when applying states. This
        can also be set in the minion config file using the
        :conf_minion:`pillarenv` option. When neither the
        :conf_minion:`pillarenv` minion config option nor this CLI argument is
        used, all Pillar environments will be merged together.

        .. versionadded:: 2018.3.0

    pillar
        Custom Pillar values, passed as a dictionary of key-value pairs

        .. note::
            Values passed this way will override Pillar values set via
            ``pillar_roots`` or an external Pillar source.

        .. versionadded:: 2018.3.0

    CLI Example:

    .. code-block:: bash

        salt myminion docker.sls compassionate_mirzakhani mods=rails,web

    '''
    mods = [item.strip() for item in mods.split(',')] if mods else []

    # Figure out the saltenv/pillarenv to use
    pillar_override = kwargs.pop('pillar', None)
    if 'saltenv' not in kwargs:
        kwargs['saltenv'] = 'base'
    sls_opts = __utils__['state.get_sls_opts'](__opts__, **kwargs)

    # gather grains from the container
    grains = call(name, 'grains.items')

    # compile pillar with container grains
    pillar = salt.pillar.get_pillar(
        __opts__,
        grains,
        __opts__['id'],
        pillar_override=pillar_override,
        pillarenv=sls_opts['pillarenv']).compile_pillar()
    if pillar_override and isinstance(pillar_override, dict):
        pillar.update(pillar_override)

    trans_tar = _prepare_trans_tar(
        name,
        sls_opts,
        mods=mods,
        pillar=pillar,
        extra_filerefs=kwargs.get('extra_filerefs', ''))

    # where to put the salt trans tar
    trans_dest_path = _generate_tmp_path()
    mkdirp_trans_argv = ['mkdir', '-p', trans_dest_path]
    # put_archive requires the path to exist
    ret = run_all(name, subprocess.list2cmdline(mkdirp_trans_argv))
    if ret['retcode'] != 0:
        return {'result': False, 'comment': ret['stderr']}

    ret = None
    try:
        trans_tar_sha256 = __utils__['hashutils.get_hash'](trans_tar, 'sha256')
        copy_to(name,
                trans_tar,
                os.path.join(trans_dest_path, 'salt_state.tgz'),
                exec_driver=_get_exec_driver(),
                overwrite=True)

        # Now execute the state into the container
        ret = call(name,
                   'state.pkg',
                   os.path.join(trans_dest_path, 'salt_state.tgz'),
                   trans_tar_sha256,
                   'sha256')
    finally:
        # delete the trans dir so that it does not end in the image
        rm_trans_argv = ['rm', '-rf', trans_dest_path]
        run_all(name, subprocess.list2cmdline(rm_trans_argv))
        # delete the local version of the trans tar
        try:
            os.remove(trans_tar)
        except (IOError, OSError) as exc:
            log.error(
                'docker.sls: Unable to remove state tarball \'%s\': %s',
                trans_tar, exc
            )
    if not isinstance(ret, dict):
        __context__['retcode'] = 1
    elif not __utils__['state.check_result'](ret):
        __context__['retcode'] = 2
    else:
        __context__['retcode'] = 0
    return ret